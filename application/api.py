from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from application import crud
from application.dependencies import get_session
from application import schemas

router = APIRouter()


@router.post('/aircraft/', response_model=schemas.Aircraft, status_code=201, tags=["aircraft"])
async def create_aircraft(aircraft: schemas.Aircraft, session: Session = Depends(get_session)):
    return crud.create_aircraft(session, aircraft)


@router.get('/aircraft/', response_model=list[schemas.Aircraft], tags=["aircraft"])
def read_aircrafts(skip: int = 0, limit: int = 100, session: Session = Depends(get_session)):
    return crud.get_aircrafts(session, skip=skip, limit=limit)
