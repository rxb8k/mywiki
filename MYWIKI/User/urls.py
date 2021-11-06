from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = "User"

urlpatterns = [
    path('signup', views.signup_view, name="signup"),
    path('login', views.login_view, name="login"),
    path('logout', views.logout_view, name="logout"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)