from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class Aircraft(BaseModel):
    serial_number: str
    manufacturer: Optional[str]

    class Config:
        orm_mode = True


class Flight(BaseModel):
    id: Optional[UUID]
    aircraft_serial_number: Optional[str]
    arrival: datetime
    arrival_airport: str
    departure: datetime
    departure_airport: str

    class Config:
        orm_mode = True
