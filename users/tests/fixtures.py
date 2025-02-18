import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def create_user(db):
    def make_user(**kwargs):
        return get_user_model().objects.create_user(**kwargs)
    return make_user


@pytest.fixture
def admin_user(create_user):
    return create_user(username='admin', password='adminpass', is_admin=True)


@pytest.fixture
def normal_user(create_user):
    return create_user(username='user', password='userpass', is_admin=False)