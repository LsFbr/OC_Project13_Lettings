"""Unit tests for models in the lettings app."""

import pytest
from lettings.models import Address, Letting


@pytest.mark.django_db
def test_address_str():
    """Ensure Address __str__ returns the correct format."""
    address = Address.objects.create(
        number=10,
        street="Main Street",
        city="Paris",
        state="FR",
        zip_code=75000,
        country_iso_code="FRA",
    )
    assert str(address) == "10 Main Street"


@pytest.mark.django_db
def test_letting_str():
    """Ensure Letting __str__ returns the title."""
    address = Address.objects.create(
        number=10,
        street="Main Street",
        city="Paris",
        state="FR",
        zip_code=75000,
        country_iso_code="FRA",
    )
    letting = Letting.objects.create(title="My letting", address=address)

    assert str(letting) == "My letting"


@pytest.mark.django_db
def test_letting_address_relationship():
    """Ensure a Letting is correctly linked to an Address."""
    address = Address.objects.create(
        number=1,
        street="Test Street",
        city="Lyon",
        state="FR",
        zip_code=69000,
        country_iso_code="FRA",
    )
    letting = Letting.objects.create(title="Test letting", address=address)

    assert letting.address == address
