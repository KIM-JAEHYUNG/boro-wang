from django.shortcuts import render
from posts.models import Post
from django.db.models import Count, Avg


def index(request):
    return render(request, 'index.html')


def home(request):
    user = request.user
    posts = Post.objects.all().order_by('-created_at').annotate(likes_count=Count('likes'))
    context = {
        'user': user,
        'posts': posts
    }
    return render(request, 'home.html', context)


def brwfb(request):
    return render(request, 'brwfb.html')


def brwjob(request):
    return render(request, 'brwjob.html')


def brwuse(request):
    return render(request, 'brwuse.html')


def etc(request):
    post = Post.objects.filter(shows=4)
    return render(request, 'etc.html', {'post': post})


def exhibition(request):
    post = Post.objects.filter(shows=3)
    return render(request, 'exhibition.html', {'post': post})


def music(request):
    post = Post.objects.filter(shows=0)
    return render(request, 'music.html', {'post': post})


def play(request):
    post = Post.objects.filter(shows=1)
    return render(request, 'play.html', {'post': post})


def sport(request):
    post = Post.objects.filter(shows=2)
    return render(request, 'sport.html', {'post': post})


# 구 선택

def gangseo(request):
    post = Post.objects.filter(areas=0)
    return render(request, 'gangseo.html', {'post': post})


def gangnam(request):
    post = Post.objects.filter(areas=1)
    return render(request, 'gangnam.html', {'post': post})


def gangdong(request):
    post = Post.objects.filter(areas=2)
    return render(request, 'gangdong.html', {'post': post})


def gangbuk(request):
    post = Post.objects.filter(areas=3)
    return render(request, 'gangbuk.html', {'post': post})


def guro(request):
    post = Post.objects.filter(areas=4)
    return render(request, 'guro.html', {'post': post})


def geumchon(request):
    post = Post.objects.filter(areas=5)
    return render(request, 'geumchon.html', {'post': post})


def guanak(request):
    post = Post.objects.filter(areas=6)
    return render(request, 'guanak.html', {'post': post})


def gwnagjin(request):
    post = Post.objects.filter(areas=7)
    return render(request, 'gwnagjin.html', {'post': post})


def nowon(request):
    post = Post.objects.filter(areas=8)
    return render(request, 'nowon.html', {'post': post})


def dobong(request):
    post = Post.objects.filter(areas=9)
    return render(request, 'dobong.html', {'post': post})


def dongdaemun(request):
    post = Post.objects.filter(areas=10)
    return render(request, 'dongdaemun.html', {'post': post})


def dongjak(request):
    post = Post.objects.filter(areas=11)
    return render(request, 'dongjak.html', {'post': post})


def mapo(request):
    post = Post.objects.filter(areas=12)
    return render(request, 'mapo.html', {'post': post})


def seodaemoon(request):
    post = Post.objects.filter(areas=13)
    return render(request, 'seodaemoon.html', {'post': post})


def seocho(request):
    post = Post.objects.filter(areas=14)
    return render(request, 'seocho.html', {'post': post})


def seongdong(request):
    post = Post.objects.filter(areas=15)
    return render(request, 'seongdong.html', {'post': post})


def songpa(request):
    post = Post.objects.filter(areas=16)
    return render(request, 'songpa.html', {'post': post})


def seongbuk(request):
    post = Post.objects.filter(areas=17)
    return render(request, 'seongbuk.html', {'post': post})


def yongsan(request):
    post = Post.objects.filter(areas=18)
    return render(request, 'yongsan.html', {'post': post})


def yangchon(request):
    post = Post.objects.filter(areas=19)
    return render(request, 'yangchon.html', {'post': post})


def eunpyeong(request):
    post = Post.objects.filter(areas=20)
    return render(request, 'eunpyeong.html', {'post': post})


def yeongdeungpo(request):
    post = Post.objects.filter(areas=21)
    return render(request, 'yeongdeungpo.html', {'post': post})


def jongro(request):
    post = Post.objects.filter(areas=22)
    return render(request, 'jongro.html', {'post': post})


def jung(request):
    post = Post.objects.filter(areas=23)
    return render(request, 'jung.html', {'post': post})


def junglang(request):
    post = Post.objects.filter(areas=24)
    return render(request, 'junglang.html', {'post': post})
