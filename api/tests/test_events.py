import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
def test_can_create_event():
    ...


@pytest.mark.django_db
def test_can_get_events_list(api_client):
    url = reverse('event-list')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.data, list)
