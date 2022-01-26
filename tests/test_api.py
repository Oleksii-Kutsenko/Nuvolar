from unittest import mock

from application import schemas
from tests.factories import AircraftFactory


def test_create_aircraft(client):
    aircraft = schemas.Aircraft.from_orm(AircraftFactory.build())

    response = client.post(
        '/aircraft/',
        json=aircraft.dict()
    )

    assert response.status_code == 201
    assert response.json() == aircraft.dict()


@mock.patch('application.crud.get_aircrafts', return_value=[])
def test_read_aircraft(mock_get_aircrafts, client, session):
    client.get(
        '/aircraft/'
    )
    mock_get_aircrafts.assert_called_with(session, skip=0, limit=100)

    client.get(
        '/aircraft/?skip=5'
    )
    mock_get_aircrafts.assert_called_with(session, skip=5, limit=100)

    client.get(
        '/aircraft/?limit=50'
    )
    mock_get_aircrafts.assert_called_with(session, skip=0, limit=50)

    client.get(
        '/aircraft/?skip=10&limit=40'
    )
    mock_get_aircrafts.assert_called_with(session, skip=10, limit=40)
