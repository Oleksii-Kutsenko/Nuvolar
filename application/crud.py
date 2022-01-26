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
