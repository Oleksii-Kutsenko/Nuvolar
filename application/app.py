import os

from fastapi import FastAPI

from application.api.aircraft import aircraft_router
from manage import configure_app


def create_app():
    configure_app(os.environ['FASTAPI_ENV'])
    app = FastAPI()

    app.include_router(aircraft_router)

    return app
