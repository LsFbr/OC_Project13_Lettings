"""Tests for URL routing in the oc_lettings_site app."""

from django.urls import resolve, reverse


def test_index_url():
    """Ensure the index URL is correct."""
    path = reverse("index")
    assert path == "/"
    assert resolve(path).view_name == "index"
