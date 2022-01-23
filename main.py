import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi_sqlalchemy import db

from models import Aircraft as ModelAircraft
from schemas import Aircraft as SchemaAircraft

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, '.env'))

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])


@app.get('/')
async def root():
    return {'name': 'Fleet API 0.0.1'}


@app.post('/aircraft/', response_model=SchemaAircraft)
def create_aircraft(aircraft: SchemaAircraft):
    db_aircraft = ModelAircraft(serial_number=aircraft.serial_number, manufacturer=aircraft.manufacturer)
    db.session.add(db_aircraft)
    db.session.commit()
    return db_aircraft


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
