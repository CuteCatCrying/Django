from django.shortcuts import render
from .models import Post
# Create your views here.

def index(request):
    posts = Post.objects.all()

    context = {
        'Judul': 'Home Blog',
        'Content': 'Ini adalah halaman Blog',
        'Posts': posts,
    }
    return render(request, 'blog/index.html', context)

def detailPost(request, slugInput):
    posts = Post.objects.get(slug=slugInput)

    context = {
        'Judul': 'Home Blog',
        'Content': 'Ini adalah halaman Detail Blog',
        'Posts': posts,
    }
    return render(request, 'blog/detail.html', context)