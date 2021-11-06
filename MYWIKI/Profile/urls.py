from django.urls import path

from . import views

app_name = "Profile"

urlpatterns = [
    path('read/<int:id>', views.read, name="read"),
    path('update/<int:id>', views.update, name="update"),
]