"""Tests for URL routing in the lettings app."""

from django.urls import resolve, reverse


def test_index_url():
    """Ensure the index URL is correct."""
    path = reverse("lettings:index")
    assert path == "/lettings/"
    assert resolve(path).view_name == "lettings:index"


def test_letting_url():
    """Ensure the letting URL is correct."""
    path = reverse("lettings:letting", args=[1])
    assert path == "/lettings/1/"
    assert resolve(path).view_name == "lettings:letting"
