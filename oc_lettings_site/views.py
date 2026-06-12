"""Views for the main OC Lettings site.

This module handles global pages such as the home page.
"""
import logging

from django.shortcuts import render
from django.conf import settings
from django.urls import is_valid_path
from sentry_sdk import capture_message

logger = logging.getLogger(__name__)


def index(request):
    logger.info("Home page requested")
    return render(request, "index.html")


# For testing 500 errors
def trigger_500_error(request):
    """
    Raise a server error to test the custom 500 page and verify Sentry error tracking.

    :param request: HTTP request
    :raises ZeroDivisionError: Always raised to simulate a server error
    """
    logger.info("Sentry test error route requested")
    return 1 / 0


def custom_404(request, exception):
    """
    Render the custom 404 page and report the error to Sentry.

    :param request: HTTP request
    :param exception: Exception that caused the 404 error
    :return: Rendered custom 404 page
    """
    # Case where the URL is first entered without a trailing slash
    # and then redirected with a trailing slash by Django APPEND_SLASH setting
    # example: /lettings/1 -> /lettings/1/
    if (
        settings.APPEND_SLASH
        and not request.path.endswith("/")
        and is_valid_path(f"{request.path}/")
    ):
        logger.info(
            "Skipping Sentry report for URL redirected with trailing slash: %s",
            request.path,
        )
        return render(request, "404.html", status=404)

    message = f"404 Not Found: {request.method} {request.path}"

    logger.warning(message)
    capture_message(message, level="warning")

    return render(request, "404.html", status=404)


def custom_500(request):
    """
    Render the custom 500 page.

    :param request: HTTP request
    :return: Rendered custom 500 page
    """
    return render(request, "500.html", status=500)
