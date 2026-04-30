"""Views for the lettings app.

Handles display of rental listings and individual letting details.
"""

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Letting


def index(request):
    """
    Display a list of all lettings.

    :param request: HTTP request
    :return: Rendered page with all lettings
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """
    Display the details of a specific letting.

    :param request: HTTP request
    :param letting_id: ID of the letting to display
    :return: Rendered page with letting details
    """
    letting = get_object_or_404(Letting, id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
