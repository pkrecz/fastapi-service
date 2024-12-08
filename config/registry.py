import logging
from config.database import engine
from config.middleware import CustomMiddleware
from fastapi.middleware.cors import CORSMiddleware


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
    logger.info("Routers has been loaded.")


def load_middleware(application):
    application.add_middleware(CustomMiddleware)
    application.add_middleware(CORSMiddleware,
                                allow_origins=["*"],
                                allow_credentials=True,
                                allow_methods=["*"],
                                allow_headers=["*"])
    logger.info("Middleware has been added.")
