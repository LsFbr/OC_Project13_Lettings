"""Views for the main OC Lettings site.

This module handles global pages such as the home page.
"""

from django.shortcuts import render


def index(request):
    """
    Render the home page.

    :param request: HTTP request
    :return: Rendered home page template
    """
    return render(request, 'index.html')


# For testing 500 errors
def trigger_500_error(request):
    """
    Raise a server error to test the custom 500 page.

    :param request: HTTP request
    :raises ZeroDivisionError: Always raised to simulate a server error
    """
    return 1 / 0
