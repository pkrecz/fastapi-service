import contextvars
from functools import wraps
from config.database import SessionLocal

db_session_context = contextvars.ContextVar("db_session", default=None)


def transactional(function):
    @wraps(function)
    def wrap_function(*args, **kwargs):
        db_session = db_session_context.get()
        if db_session is None:
            db_session = SessionLocal()
            db_session_context.set(db_session)
            try:
                result = function(*args, **kwargs)
                db_session.commit()
            except Exception as exception:
                db_session.rollback()
                raise
            finally:
                db_session.close()
                db_session_context.set(None)
        else:
            return function(*args, **kwargs)
        return result
    return wrap_function


def db(function):
    @wraps(function)
    def wrap_function(*args, **kwargs):
        db_session = db_session_context.get()
        if db_session is None:
            db_session = SessionLocal()
            db_session_context.set(db_session)
        return function(*args, **kwargs, db=db_session)
    return wrap_function
