"""URL configuration for the profiles app.

Defines routes for listing all profiles and viewing a specific user profile.
"""

from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:username>/', views.profile, name='profile'),
]
