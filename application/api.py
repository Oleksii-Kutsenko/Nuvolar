from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from application import crud
from application.dependencies import get_db
from application.schemas import Aircraft as SchemaAircraft

router = APIRouter()


@router.post('/aircraft/', response_model=SchemaAircraft, status_code=201, tags=["aircraft"])
async def create_aircraft(aircraft: SchemaAircraft, session: Session = Depends(get_db)):
    return crud.create_aircraft(session, aircraft)
