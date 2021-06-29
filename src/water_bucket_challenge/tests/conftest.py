import pytest

from ..main import application


@pytest.fixture()
def client():
    with application.test_client() as c:
        yield c
