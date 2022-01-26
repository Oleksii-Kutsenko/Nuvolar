from fastapi import Depends, APIRouter, HTTPException, Response
from sqlalchemy.orm import Session

from application import schemas
from application.crud.aircraft import AircraftCRUD
from application.dependencies import get_session

router = APIRouter()


@router.post('/aircraft/', response_model=schemas.Aircraft, status_code=201, tags=["aircraft"])
async def create_aircraft(
        aircraft: schemas.Aircraft,
        session: Session = Depends(get_session)
):
    return AircraftCRUD.create_object(session, aircraft)


@router.get('/aircraft/{serial_number}', response_model=schemas.Aircraft, tags=["aircraft"])
async def read_aircraft(
        serial_number: str,
        session: Session = Depends(get_session)
):
    aircraft = AircraftCRUD.get_object(session, serial_number)
    if aircraft:
        return aircraft
    raise HTTPException(status_code=404, detail='Aircraft not found')


@router.get('/aircraft/', response_model=list[schemas.Aircraft], tags=["aircraft"])
async def read_aircrafts(
        skip: int = 0,
        limit: int = 100,
        session: Session = Depends(get_session)
):
    return AircraftCRUD.get_objects(session, skip=skip, limit=limit)


@router.put('/aircraft/{serial_number}', response_model=schemas.Aircraft, tags=["aircraft"])
async def update_aircraft(
        serial_number: str,
        aircraft: schemas.Aircraft,
        session: Session = Depends(get_session)
):
    aircraft = AircraftCRUD.update_object(session, serial_number, aircraft)
    if aircraft:
        return aircraft
    raise HTTPException(status_code=404, detail='Aircraft not found')


@router.patch('/aircraft/{serial_number}', tags=["aircraft"])
async def partial_update_aircraft(
        serial_number: str,
        aircraft: schemas.Aircraft,
        session: Session = Depends(get_session)
):
    aircraft = AircraftCRUD.update_object(session, serial_number, aircraft)
    if aircraft:
        return aircraft
    raise HTTPException(status_code=404, detail='Aircraft not found')


@router.delete('/aircraft/{serial_number}', status_code=204)
async def delete_aircraft(
        serial_number: str,
        session: Session = Depends(get_session)
):
    removed = AircraftCRUD.delete_object(session, serial_number)
    if removed:
        return Response(status_code=204)
    raise HTTPException(status_code=404, detail='Aircraft not found')
