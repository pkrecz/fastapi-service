import logging
from config.database import engine


# app_example imports ...
from app_example import models as example_models
from app_example import controlers as example_controlers


logger = logging.getLogger("uvicorn.error")


def create_tables():
    example_models.Base.metadata.create_all(bind=engine)
    logger.info("Tables has been created.")


def load_routers(application):

    application.include_router(router=example_controlers.router,
                                prefix="",
                                tags=["Example"])
