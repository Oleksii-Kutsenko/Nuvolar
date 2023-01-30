import os

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from fastapi.testclient import TestClient
from application.database import Base
from application.main import app
from application.dependencies import get_session

SQLALCHEMY_DATABASE_URL = (
    f"postgresql+psycopg2://{os.environ['POSTGRES_USER']}:{os.environ['POSTGRES_PASSWORD']}"
    f"@{os.environ['POSTGRES_HOST']}:{os.environ['POSTGRES_PORT']}"
)


@pytest.fixture(scope="session")
def db_engine():
    engine = create_engine(SQLALCHEMY_DATABASE_URL)

    Base.metadata.create_all(bind=engine)
    yield engine


@pytest.fixture(scope="function")
def session(db_engine):
    connection = db_engine.connect()
    transaction = connection.begin()
    db = Session(bind=connection)

    yield db

    db.rollback()
    connection.close()


@pytest.fixture(scope="function")
def client(session):
    app.dependency_overrides[get_session] = lambda: session

    with TestClient(app) as test_client:
        yield test_client
