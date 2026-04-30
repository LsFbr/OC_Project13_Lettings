"""Data models for the lettings application.

Defines rental listings and their associated addresses.
"""

from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """Represents a postal address associated with a letting."""

    class Meta:
        """Override Django's default plural name for correct admin display."""
        verbose_name_plural = "Addresses"

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self):
        """Return a human-readable representation of the address."""
        return f'{self.number} {self.street}'


class Letting(models.Model):
    """Represents a rental listing linked to an address."""
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """Return a human-readable representation of the letting."""
        return self.title
