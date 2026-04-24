"""Integration tests for views in the oc_lettings_site app."""

from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed


def test_index_view(client):
    """
    Ensure the index view returns HTTP 200
    and uses the correct template with the correct content.
    """

    response = client.get(reverse("index"))
    content = response.content.decode()
    expected_content = "Welcome to Holiday Homes"

    assert expected_content in content
    assert response.status_code == 200
    assertTemplateUsed(response, "index.html")


def test_500_error_view(client):
    """
    Ensure the 500 error is returned when a server error occurs,
    and the correct template is used with the correct content.
    """

    # disable Django's default exception handling to test the status code
    client.raise_request_exception = False

    response = client.get(reverse("500-error"))
    content = response.content.decode()
    expected_content = "Server error"

    assert expected_content in content
    assert response.status_code == 500
    assertTemplateUsed(response, "500.html")


# //404 error view tests
def test_404_page(client):
    """
    Ensure the 404 error is returned when a non-existent URL is accessed,
    and the correct template is used with the correct content.
    """

    response = client.get("/url-inexistante/")
    content = response.content.decode()
    expected_content = "Page not found"

    assert expected_content in content
    assert response.status_code == 404
    assertTemplateUsed(response, "404.html")
