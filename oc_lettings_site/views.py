"""Views for the main OC Lettings site.

This module handles global pages such as the home page.
"""
import logging

from django.shortcuts import render

logger = logging.getLogger(__name__)


def index(request):
    """
    Render the home page.

    :param request: HTTP request
    :return: Rendered home page template
    """
    logger.info("Home page requested")
    return render(request, 'index.html')


# For testing 500 errors
def trigger_500_error(request):
    """
    Raise a server error to test the custom 500 page and verify Sentry error tracking.

    :param request: HTTP request
    :raises ZeroDivisionError: Always raised to simulate a server error
    """
    logger.error("Sentry test error route requested")
    return 1 / 0
