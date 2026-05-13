"""Views for the profiles app.

Handles display of user profiles and individual profile details.
"""
import logging
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Profile

logger = logging.getLogger(__name__)


def index(request):
    """
    Display a list of all user profiles.

    :param request: HTTP request
    :return: Rendered page with all profiles
    """
    logger.info("Profiles index page requested")

    try:
        profiles_list = Profile.objects.all()
        context = {'profiles_list': profiles_list}
        return render(request, 'profiles/index.html', context)
    except Exception:
        logger.exception("500 Server Error while loading profiles index page")
        raise


def profile(request, username):
    """
    Display details of a specific user profile.

    :param request: HTTP request
    :param username: Username of the profile to retrieve
    :return: Rendered page with profile details
    :raises Http404: If the profile does not exist
    """
    logger.info("Profile detail page requested", extra={"username": username})

    try:
        profile = get_object_or_404(Profile, user__username=username)
        context = {'profile': profile}
        return render(request, 'profiles/profile.html', context)
    except Http404:
        logger.warning("Profile not found for username=%s", username)
        raise
    except Exception:
        logger.exception(
            "500 Server Error while loading profile detail for username=%s",
            username,
        )
        raise

    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
