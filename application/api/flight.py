from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session

from application import schemas
from application.crud import FlightCRUD
from application.dependencies import get_session

flight_router = APIRouter()


@flight_router.post(
    '/flight/',
    response_model=schemas.Flight,
    status_code=201,
    tags=['flight']
)
async def create_flight(
        flight: schemas.Flight,
        session: Session = Depends(get_session)
):
    return FlightCRUD.create_object(session, flight)


@flight_router.get(
    '/flight/{_id}',
    response_model=schemas.Flight,
    tags=['flight']
)
async def read_flight(
        _id: UUID,
        session: Session = Depends(get_session)
):
    flight = FlightCRUD.get_object(session, _id)
    if flight:
        return flight
    raise HTTPException(status_code=404, detail='Flight not found')


@flight_router.get(
    '/flight/',
    response_model=list[schemas.Flight],
    tags=['flight']
)
async def read_flights(
        skip: int = 0,
        limit: int = 100,
        session: Session = Depends(get_session)
):
    return FlightCRUD.get_objects(session, skip=skip, limit=limit)


@flight_router.put(
    '/flight/{_id}',
    response_model=schemas.Aircraft,
    tags=["flight"]
)
async def update_aircraft(
        _id: UUID,
        flight: schemas.Flight,
        session: Session = Depends(get_session)
):
    aircraft = FlightCRUD.update_object(session, _id, flight)
    if aircraft:
        return aircraft
    raise HTTPException(status_code=404, detail='Aircraft not found')


@flight_router.patch(
    '/flight/{_id}',
    tags=["flight"]
)
async def partial_update_aircraft(
        _id: UUID,
        flight: schemas.Flight,
        session: Session = Depends(get_session)
):
    flight = FlightCRUD.update_object(session, _id, flight)
    if flight:
        return flight
    raise HTTPException(status_code=404, detail='Aircraft not found')


@flight_router.delete(
    '/flight/{_id}',
    status_code=204
)
async def delete_aircraft(
        _id: str,
        session: Session = Depends(get_session)
):
    removed = FlightCRUD.delete_object(session, _id)
    if removed:
        return Response(status_code=204)
    raise HTTPException(status_code=404, detail='Aircraft not found')
