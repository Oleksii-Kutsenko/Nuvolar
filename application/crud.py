from sqlalchemy.orm import Session

from application import models, schemas


def create_aircraft(session: Session, aircraft: schemas.Aircraft):
    db_aircraft = models.Aircraft(
        serial_number=aircraft.serial_number,
        manufacturer=aircraft.manufacturer
    )
    session.add(db_aircraft)
    session.commit()
    session.refresh(db_aircraft)
    return db_aircraft


def get_aircraft(session: Session, serial_number: str):
    aircraft = session.query(models.Aircraft).filter(models.Aircraft.serial_number == serial_number).first()
    if aircraft:
        return aircraft
    return None


def get_aircrafts(session: Session, skip: int = 0, limit: int = 100):
    return session.query(models.Aircraft).offset(skip).limit(limit).all()


def update_aircraft(session: Session, serial_number: str, aircraft: schemas.Aircraft):
    db_aircraft = session.query(models.Aircraft).filter(models.Aircraft.serial_number == serial_number).first()
    if db_aircraft is None:
        return None

    for attr, value in vars(aircraft).items():
        setattr(db_aircraft, attr, value) if value else None

    session.add(db_aircraft)
    session.commit()
    session.refresh(db_aircraft)
    return db_aircraft
