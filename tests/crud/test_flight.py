from uuid import uuid4

import pytest
from sqlalchemy.exc import IntegrityError

from application import models
from application import schemas
from application.crud.crud import AircraftCRUD
from tests.factories import AircraftFactory


def test_create_aircraft(session):
    aircraft = schemas.Aircraft(serial_number="test_serial_number", manufacturer="Airbus")
    AircraftCRUD.create_object(session, aircraft)

    assert session.query(models.Aircraft).count() == 1


def test_duplicate_create_aircraft(session):
    aircraft = schemas.Aircraft(serial_number="test_serial_number", manufacturer="Airbus")
    AircraftCRUD.create_object(session, aircraft)
    with pytest.raises(IntegrityError):
        AircraftCRUD.create_object(session, aircraft)


def test_get_aircraft(session):
    db_aircraft = AircraftFactory.build()
    session.add(db_aircraft)
    session.commit()

    aircraft = AircraftCRUD.get_object(session, db_aircraft.serial_number)
    assert aircraft.serial_number == db_aircraft.serial_number


def test_wrong_get_aircraft(session):
    aircraft = AircraftCRUD.get_object(session, str(uuid4()))
    assert aircraft is None


def test_get_aircrafts(session):
    entities_number = 10

    aircrafts = AircraftCRUD.get_objects(session)
    assert len(aircrafts) == 0

    for _ in range(entities_number):
        session.add(AircraftFactory.build())
    session.commit()

    aircrafts = AircraftCRUD.get_objects(session)
    assert len(aircrafts) == entities_number

    skip_number = 3
    aircrafts = AircraftCRUD.get_objects(session, skip_number)
    assert len(aircrafts) == (entities_number - skip_number)

    limit_number = 5
    aircrafts = AircraftCRUD.get_objects(session, 0, limit_number)
    assert len(aircrafts) == (entities_number - limit_number)


def test_wrong_update_aircraft(session):
    schema_aircraft = schemas.Aircraft(serial_number="", manufacturer="")
    aircraft = AircraftCRUD.update_object(session, str(uuid4()), schema_aircraft)

    assert aircraft is None


def test_update_aircraft(session):
    db_aircraft = AircraftFactory.build()
    session.add(db_aircraft)
    session.commit()

    new_serial_number = '-1'
    new_manufacturer = '-1'
    schema_aircraft = schemas.Aircraft(serial_number=new_serial_number, manufacturer=new_manufacturer)

    updated_aircraft = AircraftCRUD.update_object(session, db_aircraft.serial_number, schema_aircraft)

    assert updated_aircraft.serial_number == new_serial_number
    assert updated_aircraft.manufacturer == new_manufacturer


def test_delete_aircraft(session):
    pass
