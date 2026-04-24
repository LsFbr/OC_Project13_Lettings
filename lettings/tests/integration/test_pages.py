"""Integration tests for views in the lettings app."""

import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed
from lettings.models import Letting, Address


@pytest.mark.django_db
def test_index_view_empty(client):
    """Ensure the index view returns HTTP 200 and uses the correct template with the correct content."""

    response = client.get(reverse("lettings:index"))
    content = response.content.decode()
    expected_content = "No lettings are available."

    assert expected_content in content
    assert response.status_code == 200
    assertTemplateUsed(response, "lettings/index.html")

@pytest.mark.django_db
def test_index_view_not_empty(client):
    """Ensure the index view returns HTTP 200 and uses the correct template with the correct content."""

    address = Address.objects.create(
        number=10,
        street="Main Street",
        city="Paris",
        state="FR",
        zip_code=75000,
        country_iso_code="FRA",
    )
    Letting.objects.create(title="My letting", address=address)

    response = client.get(reverse("lettings:index"))
    content = response.content.decode()
    expected_content = "My letting"

    assert expected_content in content
    assert response.status_code == 200
    assertTemplateUsed(response, "lettings/index.html")


@pytest.mark.django_db
def test_letting_view(client):
    """Ensure the letting view returns HTTP 200 and uses the correct template with the correct content."""
    address = Address.objects.create(
        number=10,
        street="Main Street",
        city="Paris",
        state="FR",
        zip_code=75000,
        country_iso_code="FRA",
    )
    letting = Letting.objects.create(title="My letting", address=address)

    response = client.get(reverse("lettings:letting", args=[letting.id]))
    content = response.content.decode()
    expected_content = "Main Street"

    assert expected_content in content
    assert response.status_code == 200
    assertTemplateUsed(response, "lettings/letting.html")


@pytest.mark.django_db
def test_letting_view_not_found(client):
    """Ensure the letting view returns HTTP 404 when a non-existent letting is accessed."""

    # disable Django's default exception handling to test the status code
    client.raise_request_exception = False

    response = client.get(reverse("lettings:letting", args=[999999]))
    assert response.status_code == 404
