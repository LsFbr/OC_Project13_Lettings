"""Admin configuration for OC Lettings.

Registers models from the lettings and profiles applications
to make them accessible via the Django admin interface.
"""

from django.contrib import admin

from lettings.models import Letting
from lettings.models import Address
from profiles.models import Profile


admin.site.register(Letting)
admin.site.register(Address)
admin.site.register(Profile)
