import os

from fastapi import FastAPI

from application.api.aircraft import aircraft_router
from application.api.flight import flight_router
from manage import configure_app


def create_app():
    configure_app(os.environ['FASTAPI_ENV'])
    app = FastAPI()

    app.include_router(aircraft_router)
    app.include_router(flight_router)

    return app
