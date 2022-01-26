from application import schemas


def test_root(client):
    response = client.get('/')

    assert response.status_code == 200


def test_create_aircraft(client):
    aircraft = schemas.Aircraft(serial_number='test_serial_number', manufacturer='Airbus')
    response = client.post(
        '/aircraft/',
        json=aircraft.dict()
    )

    assert response.status_code == 201
    assert response.json() == aircraft.dict()
