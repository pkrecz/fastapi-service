from service.decorators import db, transactional
from .schemas import AuthorViewBase
from .models import AuthorModel


@transactional
@db
def create_author(input_data, db):
    instance = AuthorModel(**input_data.model_dump())
    db.add(instance)
    db.flush()
    return AuthorViewBase.model_validate(instance)


@transactional
@db
def update_author(id, input_data, db):
    query = db.query(AuthorModel).filter_by(id=id)
    query.update(input_data.model_dump())
    db.flush()
    instance = query.first()
    return AuthorViewBase.model_validate(instance)


@transactional
@db
def delete_author(id, db):
    query = db.query(AuthorModel).filter_by(id=id)
    db.delete(query.first())
    db.flush()
    return str("Author has been deleted.")


@db
def retrieve_author(id, db):
    query = db.query(AuthorModel).filter_by(id=id)
    instance = query.first()
    return AuthorViewBase.model_validate(instance)


@db
def list_author(db):
    output = list()
    query = db.query(AuthorModel)
    instance = query.all()
    for item in instance:
        output.append(AuthorViewBase.model_validate(item))
    return list(output)
