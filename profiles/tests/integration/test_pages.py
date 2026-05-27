"""Integration tests for views in the profiles app."""

import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from pytest_django.asserts import assertTemplateUsed
from profiles.models import Profile


@pytest.mark.django_db
def test_index_view_empty(client):
    """Ensure index page works with no profiles."""

    response = client.get(reverse("profiles:index"))
    content = response.content.decode()
    expected_content = "No profiles are available."

    assert expected_content in content
    assert response.status_code == 200
    assertTemplateUsed(response, "profiles/index.html")


@pytest.mark.django_db
def test_index_view_not_empty(client):
    """Ensure index page displays profiles."""

    user = User.objects.create(username="john")
    Profile.objects.create(user=user, favorite_city="Paris")

    response = client.get(reverse("profiles:index"))
    content = response.content.decode()
    expected_content = "john"

    assert expected_content in content
    assert response.status_code == 200
    assertTemplateUsed(response, "profiles/index.html")


@pytest.mark.django_db
def test_profile_view(client):
    """Ensure profile detail page works."""

    user = User.objects.create(username="john")
    Profile.objects.create(user=user, favorite_city="Paris")

    response = client.get(reverse("profiles:profile", args=["john"]))
    content = response.content.decode()
    expected_content = "Paris"

    assert expected_content in content
    assert response.status_code == 200
    assertTemplateUsed(response, "profiles/profile.html")


@pytest.mark.django_db
def test_profile_view_not_found(client):
    """Ensure 404 is returned when a non-existent user is accessed."""

    client.raise_request_exception = False

    response = client.get(reverse("profiles:profile", args=["unknown"]))

    assert response.status_code == 404
