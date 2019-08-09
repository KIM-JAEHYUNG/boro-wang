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


def gangseo(request):
    post = Post.objects.filter(areas=15)
    postt = Post.objects.filter(shows=1)
    return render(request, 'gangseo.html', {'post': post&postt})


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
