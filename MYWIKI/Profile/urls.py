from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('read/<int:id>', views.read, name="read"),
    path('update/<int:id>', views.update, name="update"),
    path('history/<int:id>', views.view_history, name="view_history")
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)