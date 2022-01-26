import pytest
from sqlalchemy.exc import IntegrityError

from application import models
from application import schemas
from application.crud import create_aircraft, get_aircrafts
from tests.factories import AircraftFactory


def test_create_aircraft(session):
    aircraft = schemas.Aircraft(serial_number="test_serial_number", manufacturer="Airbus")
    create_aircraft(session, aircraft)

    assert session.query(models.Aircraft).count() == 1


def test_duplicate_create_aircraft(session):
    aircraft = schemas.Aircraft(serial_number="test_serial_number", manufacturer="Airbus")
    create_aircraft(session, aircraft)
    with pytest.raises(IntegrityError):
        create_aircraft(session, aircraft)


def test_get_aircrafts(session):
    entities_number = 10

    aircrafts = get_aircrafts(session)
    assert len(aircrafts) == 0

    for _ in range(entities_number):
        session.add(AircraftFactory.build())
    session.commit()

    aircrafts = get_aircrafts(session)
    assert len(aircrafts) == entities_number

    skip_number = 3
    aircrafts = get_aircrafts(session, skip_number)
    assert len(aircrafts) == (entities_number - skip_number)

    limit_number = 5
    aircrafts = get_aircrafts(session, 0, limit_number)
    assert len(aircrafts) == (entities_number - limit_number)
