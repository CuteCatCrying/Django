from django.shortcuts import render
from .models import Post
# Create your views here.

def index(request):
    posts = Post.objects.all()
    categories = Post.objects.values('category').distinct()
    print(categories)

    context = {
        'Judul': 'Home Blog',
        'Content': 'Ini adalah halaman Blog',
        'Categories': categories,
        'Posts': posts,
    }
    return render(request, 'blog/index.html', context)

def categoryPost(request, categoryInput):
    posts = Post.objects.filter(category=categoryInput)
    categories = Post.objects.values('category').distinct()
    print(categories)

    context = {
        'Judul': 'Home Blog',
        'Content': 'tampilkan berdasarkan category',
        'Categories': categories,
        'Posts': posts,
    }
    return render(request, 'blog/category.html', context)

def detailPost(request, slugInput):
    posts = Post.objects.get(slug=slugInput)
    categories = Post.objects.values('category').distinct()
    print(categories)

    context = {
        'Judul': 'Home Blog',
        'Content': 'Ini adalah halaman Detail Blog',
        'Categories': categories,
        'Posts': posts,
    }
    return render(request, 'blog/detail.html', context)