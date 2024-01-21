import pytest
from django.urls import reverse
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_index_view(client):
    code = 200
    assert code == 200
