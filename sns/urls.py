from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import index
from .views import home
from .views import brwfb
from .views import brwjob
from .views import brwuse


urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path('', index, name="index"),
    path('home/', home, name='home'),
    path('brwfb/', brwfb, name='brwfb'),
    path('brwjob/', brwjob, name='brwjob'),
    path('brwuse/', brwuse, name='brwuse'),
    path('accounts/', include('allauth.urls')),
    path('users/', include('users.urls')),
    path('posts/', include('posts.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
