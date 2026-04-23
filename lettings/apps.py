"""Application configuration for the lettings app.

This app manages rental listings and their associated addresses.
"""

from django.apps import AppConfig


class LettingsConfig(AppConfig):
    """Configuration class for the lettings Django application."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lettings'
