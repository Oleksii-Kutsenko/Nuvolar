import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import crud
import models
from database import engine, SessionLocal
from schemas import Aircraft as SchemaAircraft

# TODO: Create Settings Class
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, '.env'))

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
