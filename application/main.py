import os

import uvicorn
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from application import crud
from application import models
from application.database import engine, SessionLocal
from manage import configure_app
from application.schemas import Aircraft as SchemaAircraft

configure_app(os.environ['FASTAPI_ENV'])

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/')
async def root():
    return {'name': os.environ['API_NAME']}


@app.post('/aircraft/', response_model=SchemaAircraft)
def create_aircraft(aircraft: SchemaAircraft, db: Session = Depends(get_db)):
    return crud.create_aircraft(db, aircraft)


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
