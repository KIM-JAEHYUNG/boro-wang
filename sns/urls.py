from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import index
from .views import home
from .views import brwfb
from .views import brwjob
from .views import brwuse
from .views import gangseo
from .views import play
from .views import exhibition
from .views import etc
from .views import sport
from .views import music


urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path('', index, name="index"),
    path('home/', home, name='home'),
    path('brwfb/', brwfb, name='brwfb'),
    path('brwjob/', brwjob, name='brwjob'),
    path('brwuse/', brwuse, name='brwuse'),
    path('gangseo/', gangseo, name="gangseo"),
    path('play/', play, name="play"),
    path('sport/', sport, name="sport"),
    path('etc/', etc, name="etc"),
    path('exhibition/', exhibition, name="exhibition"),
    path('music/', music, name="music"),
    path('accounts/', include('allauth.urls')),
    path('users/', include('users.urls')),
    path('posts/', include('posts.urls')),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
