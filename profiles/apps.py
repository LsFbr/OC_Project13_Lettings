"""Application configuration for the profiles app.

This app manages user profiles and their additional information.
"""

from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """Configuration class for the profiles Django application."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'
