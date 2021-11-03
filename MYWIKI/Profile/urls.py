from django.urls import path

from . import views as profile_views
from Profile.views import *

app_name = "Profile"

urlpatterns = [
    path('Profile/', Profile.views, name="Profile"),
    path('profile_create/', views.profile_create, name='profile_create'),
]