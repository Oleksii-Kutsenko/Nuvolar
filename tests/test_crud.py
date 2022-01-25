import pytest
from sqlalchemy.exc import IntegrityError

from application.crud import create_aircraft
from application import schemas
from application import models


def test_create_aircraft(db):
    aircraft = schemas.Aircraft(serial_number="test_serial_number", manufacturer="Airbus")
    create_aircraft(db, aircraft)

    assert db.query(models.Aircraft).count() == 1


def test_duplicate_create_aircraft(db):
    aircraft = schemas.Aircraft(serial_number="test_serial_number", manufacturer="Airbus")
    create_aircraft(db, aircraft)
    with pytest.raises(IntegrityError):
        create_aircraft(db, aircraft)
