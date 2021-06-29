from http import HTTPStatus

from flask.testing import FlaskClient


def test_water_bucket_valid(client: FlaskClient):
    response = client.post(
        '/water-bucket',
        json={'x_gallon': 2, 'y_gallon': 10, 'target': 4},
    )
    assert response.status_code == HTTPStatus.OK
    assert len(response.json) == 4


def test_water_bucket_unprocessable(client: FlaskClient):
    response = client.post(
        '/water-bucket',
        json={'x_gallon': 2, 'y_gallon': 10, 'target': 3},
    )
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


def test_water_bucket_bad_request(client: FlaskClient):
    response = client.post(
        '/water-bucket',
        json={'sdfasdf': 3},
    )
    assert response.status_code == HTTPStatus.BAD_REQUEST
