from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Aircraft(Base):
    __tablename__ = "aircrafts"

    serial_number = Column(String, primary_key=True, index=True)
    manufacturer = Column(String, index=True)
