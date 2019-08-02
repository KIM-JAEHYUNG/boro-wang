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
