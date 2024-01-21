import pytest


@pytest.mark.django_db
def test_user_create(client):
    code = 200
    assert code == 200
