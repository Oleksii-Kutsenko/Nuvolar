import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from application.main import app
from application.database import Base

SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{os.environ['POSTGRES_USER']}:{os.environ['POSTGRES_PASSWORD']}" \
                          f"@{os.environ['TEST_POSTGRES_DB']}:5432"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db
