import pytest
from rest_framework.test import APIClient, APIRequestFactory


@pytest.fixture
def api_client():
    """
    Wrapper around Django Rest Framework testing APIClient

    """

    return APIClient()


@pytest.fixture
def api_rf():
    return APIRequestFactory()
