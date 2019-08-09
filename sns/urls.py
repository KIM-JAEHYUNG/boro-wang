from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path('', index, name="index"),
    path('home/', home, name='home'),
    path('brwfb/', brwfb, name='brwfb'),
    path('brwjob/', brwjob, name='brwjob'),
    path('brwuse/', brwuse, name='brwuse'),
    # 구 선택
    path('gangseo/', gangseo, name="gangseo"),
    path('gangnam/', gangnam, name="gangnam"),
    path('gangdong/', gangdong, name="gangdong"),
    path('gangbuk/', gangbuk, name="gangbuk"),
    path('guro/', guro, name="guro"),
    path('geumchon/', geumchon, name="geumchon"),
    path('guanak/', guanak, name="guanak"),
    path('gwnagjin/', gwnagjin, name="gwnagjin"),
    path('nowon/', nowon, name="nowon"),
    path('dobong/', dobong, name="dobong"),
    path('dongdaemun/', dongdaemun, name="dongdaemun"),
    path('dongjak/', dongjak, name="dongjak"),
    path('mapo/', mapo, name="mapo"),
    path('seodaemoon/', seodaemoon, name="seodaemoon"),
    path('seocho/', seocho, name="seocho"),
    path('seongdong/', seongdong, name="seongdong"),
    path('songpa/', songpa, name="songpa"),
    path('seongbuk/', seongbuk, name="seongbuk"),
    path('yongsan/', yongsan, name="yongsan"),
    path('yangchon/', yangchon, name="yangchon"),
    path('eunpyeong/', eunpyeong, name="eunpyeong"),
    path('yeongdeungpo/', yeongdeungpo, name="yeongdeungpo"),
    path('jongro/', jongro, name="jongro"),
    path('jung/', jung, name="jung"),
    path('junglang/', junglang, name="junglang"),
    # 구 선택 끝
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
