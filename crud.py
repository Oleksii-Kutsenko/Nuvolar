from sqlalchemy.orm import Session

import models
import schemas


def create_aircraft(db: Session, aircraft: schemas.Aircraft):
    db_aircraft = models.Aircraft(serial_number=aircraft.serial_number, manufacturer=aircraft.manufacturer)
    db.add(db_aircraft)
    db.commit()
    db.refresh(db_aircraft)
    return db_aircraft
