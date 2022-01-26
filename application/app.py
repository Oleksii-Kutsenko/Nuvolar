import os

from fastapi import FastAPI

from application.api import router
from manage import configure_app


def create_app():
    configure_app(os.environ['FASTAPI_ENV'])
    app = FastAPI()

    app.include_router(router)

    return app
