from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
import sys
sys.path.append("..")
from Profile import views as profile_views
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', profile_views.home, name="home"),

    path('profile/', include('Profile.urls')),
    path('user/', include('User.urls'))
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)