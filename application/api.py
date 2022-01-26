from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from application import crud
from application.dependencies import get_session
from application import schemas

router = APIRouter()


@router.post('/aircraft/', response_model=schemas.Aircraft, status_code=201, tags=["aircraft"])
async def create_aircraft(
        aircraft: schemas.Aircraft,
        session: Session = Depends(get_session)
):
    return crud.create_aircraft(session, aircraft)


@router.get('/aircraft/{serial_number}', response_model=schemas.Aircraft)
async def read_aircraft(
        serial_number: str,
        session: Session = Depends(get_session)
):
    aircraft = crud.get_aircraft(session, serial_number)
    if aircraft:
        return aircraft
    raise HTTPException(status_code=404, detail='Aircraft not found')


@router.get('/aircraft/', response_model=list[schemas.Aircraft], tags=["aircraft"])
async def read_aircrafts(
        skip: int = 0,
        limit: int = 100,
        session: Session = Depends(get_session)
):
    return crud.get_aircrafts(session, skip=skip, limit=limit)


@router.put('/aircraft/{serial_number}', response_model=schemas.Aircraft)
async def update_aircraft(
        serial_number: str,
        aircraft: schemas.Aircraft,
        session: Session = Depends(get_session)
):
    aircraft = crud.update_aircraft(session, serial_number, aircraft)
    if aircraft:
        return aircraft
    raise HTTPException(status_code=404, detail='Aircraft not found')


@router.patch('/aircraft/{serial_number}')
async def partial_update_aircraft(
        serial_number: str,
        aircraft: schemas.Aircraft,
        session: Session = Depends(get_session)
):
    aircraft = crud.update_aircraft(session, serial_number, aircraft)
    if aircraft:
        return aircraft
    raise HTTPException(status_code=404, detail='Aircraft not found')
