"""Data models for the profiles application.

Defines user profiles associated with Django's built-in User model.
"""

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Represents additional information linked to a Django User."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """Return the username associated with the profile."""
        return self.user.username
