"""Tests for URL routing in the profiles app."""

from django.urls import resolve, reverse


def test_index_url():
    """Ensure index URL is correct."""
    path = reverse("profiles:index")
    assert path == "/profiles/"
    assert resolve(path).view_name == "profiles:index"


def test_profile_url():
    """Ensure profile URL is correct."""
    path = reverse("profiles:profile", args=["john"])
    assert path == "/profiles/john/"
    assert resolve(path).view_name == "profiles:profile"