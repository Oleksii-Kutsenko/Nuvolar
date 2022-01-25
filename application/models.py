from sqlalchemy import Column, String

from application.database import Base


class Aircraft(Base):
    __tablename__ = "aircrafts"

    serial_number = Column(String, primary_key=True, index=True)
    manufacturer = Column(String, index=True)
