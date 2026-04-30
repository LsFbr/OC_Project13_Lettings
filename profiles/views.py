"""Views for the profiles app.

Handles display of user profiles and individual profile details.
"""
import logging
from django.shortcuts import render, get_object_or_404
from .models import Profile

logger = logging.getLogger(__name__)


def index(request):
    """
    Display a list of all user profiles.

    :param request: HTTP request
    :return: Rendered page with all profiles
    """
    logger.info("Profiles index page requested")
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """
    Display details of a specific user profile.

    :param request: HTTP request
    :param username: Username of the profile to retrieve
    :return: Rendered page with profile details
    """
    logger.info("Profile detail page requested", extra={"username": username})
    profile = get_object_or_404(Profile, user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
