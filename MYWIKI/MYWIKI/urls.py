from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
import sys
sys.path.append("..")

from Profile import views as profile_views
from User import views as user_view
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', profile_views.home, name="home"),
    # path('home', profile_views.home, name="home2"),
    
    path('profile/read/<int:id>', profile_views.read, name="read"),
    path('profile/update/<int:id>', profile_views.update, name="update"),
    path('profile/history/<int:id>', profile_views.view_history, name="view_history"),


    path('user/signup', user_view.signup_view, name="signup"),
    path('user/login', user_view.login_view, name="login"),
    path('user/logout', user_view.logout_view, name="logout"),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)