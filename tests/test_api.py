from unittest import mock
from uuid import uuid4

from application import schemas
from tests.factories import AircraftFactory


def test_create_aircraft(client):
    aircraft = schemas.Aircraft.from_orm(AircraftFactory.build())

    response = client.post("/aircraft/", json=aircraft.dict())

    assert response.status_code == 201
    assert response.json() == aircraft.dict()


@mock.patch(
    "application.crud.AircraftCRUD.get_object", return_value=AircraftFactory.build()
)
def test_read_aircraft(mock_get_aircraft, client, session):
    db_aircraft = AircraftFactory.build()
    session.add(db_aircraft)
    session.commit()

    client.get(f"/aircraft/{db_aircraft.serial_number}")
    mock_get_aircraft.assert_called_with(session, db_aircraft.serial_number)


@mock.patch("application.crud.AircraftCRUD.get_object", return_value=None)
def test_wrong_read_aircraft(mock_get_aircraft, client, session):
    response = client.get(f"/aircraft/{uuid4()}")
    assert response.status_code == 404


@mock.patch("application.crud.AircraftCRUD.get_objects", return_value=[])
def test_read_aircrafts(mock_get_aircrafts, client, session):
    client.get("/aircraft/")
    mock_get_aircrafts.assert_called_with(session, skip=0, limit=100)

    client.get("/aircraft/?skip=5")
    mock_get_aircrafts.assert_called_with(session, skip=5, limit=100)

    client.get("/aircraft/?limit=50")
    mock_get_aircrafts.assert_called_with(session, skip=0, limit=50)

    client.get("/aircraft/?skip=10&limit=40")
    mock_get_aircrafts.assert_called_with(session, skip=10, limit=40)


def test_wrong_update_aircraft(client):
    schema_aircraft = schemas.Aircraft(serial_number="-1", manufacturer="-1")

    response = client.put("/aircraft/-1", json=schema_aircraft.dict())
    assert response.status_code == 404


def test_wrong_partial_update_aircraft(client):
    schema_aircraft = schemas.Aircraft(serial_number="-1")
    response = client.patch("/aircraft/-1", json=schema_aircraft.dict())
    assert response.status_code == 404


@mock.patch(
    "application.crud.AircraftCRUD.update_object", return_value=AircraftFactory.build()
)
def test_update_aircraft(mock_update_aircraft, client, session):
    db_aircraft = AircraftFactory.build()
    session.add(db_aircraft)
    session.commit()

    schema_aircraft = schemas.Aircraft.from_orm(db_aircraft)
    schema_aircraft.serial_number = "-1"
    schema_aircraft.manufacturer = "-1"

    client.put(f"/aircraft/{db_aircraft.serial_number}", json=schema_aircraft.dict())
    mock_update_aircraft.assert_called_with(
        session, db_aircraft.serial_number, schema_aircraft
    )


@mock.patch(
    "application.crud.AircraftCRUD.update_object", return_value=AircraftFactory.build()
)
def test_partial_update_aircraft(mock_partial_update_aircraft, client, session):
    db_aircraft = AircraftFactory.build()
    session.add(db_aircraft)
    session.commit()

    schema_aircraft = schemas.Aircraft.from_orm(db_aircraft)
    schema_aircraft.serial_number = "-1"

    client.patch(f"/aircraft/{db_aircraft.serial_number}", json=schema_aircraft.dict())
    mock_partial_update_aircraft.assert_called_with(
        session, db_aircraft.serial_number, schema_aircraft
    )
