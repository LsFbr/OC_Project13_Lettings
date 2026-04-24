"""Unit tests for models in the profiles app."""

import pytest
from django.contrib.auth.models import User
from profiles.models import Profile


@pytest.mark.django_db
def test_profile_str():
    """Ensure Profile __str__ returns the username."""

    user = User.objects.create(username="john")
    profile = Profile.objects.create(user=user, favorite_city="Paris")

    assert str(profile) == "john"


@pytest.mark.django_db
def test_profile_user_relationship():
    """Ensure a Profile is correctly linked to a User."""
    user = User.objects.create(username="john")
    profile = Profile.objects.create(user=user, favorite_city="Paris")

    assert profile.user == user
