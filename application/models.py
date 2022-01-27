import uuid

from sqlalchemy import Column, String, ForeignKey, DateTime, CheckConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from application.database import Base


class Aircraft(Base):
    __tablename__ = 'aircrafts'

    flights = relationship('Flight', back_populates='aircraft')
    serial_number = Column(String, primary_key=True, index=True)
    manufacturer = Column(String, index=True)


class Flight(Base):
    __tablename__ = 'flights'
    __table_args__ = (
        CheckConstraint('departure < arrival'),
        CheckConstraint('CURRENT_TIMESTAMP < departure')
    )

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    aircraft_serial_number = Column(String, ForeignKey('aircrafts.serial_number'), nullable=True)
    aircraft = relationship('Aircraft', back_populates='flights')
    arrival = Column(DateTime(timezone=True))
    arrival_airport = Column(String(4), doc='ICAO code for the arrival airport')
    departure = Column(DateTime(timezone=True))
    departure_airport = Column(String(4), doc='ICAO code for the departure airport')
