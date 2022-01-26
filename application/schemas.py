from typing import Optional

from pydantic import BaseModel


class Aircraft(BaseModel):
    serial_number: str
    manufacturer: Optional[str]

    class Config:
        orm_mode = True
