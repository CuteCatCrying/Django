from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Post

def index(request):
    str = '<h1>Home Blog</h1'
    return HttpResponse(str)

def categoryPost(request, categoryInput):
    posts = Post.objects.filter(category=categoryInput)
    print(posts)
    return HttpResponse('category post')

def singlePost(request, slugInput):
    posts = Post.objects.get(slug=slugInput)
    judul = '<h1>{}</h1>'.format(posts.judul)
    body = '<p>{}</p>'.format(posts.body)
    category = '<p>{}</p>'.format(posts.category)
    slug = '<p>{}</p>'.format(posts.slug)

    return HttpResponse(judul + body + category + slug)