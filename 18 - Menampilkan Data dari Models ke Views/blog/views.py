from django.shortcuts import render
from .models import Post
# Create your views here.

def index(request):
    # queryset
    posts = Post.objects.all()

    context = {
        'Title': 'Blog',
        'Heading': 'Blog di My Website',
        'Posts': posts,
    }
    return render(request, 'blog/index.html', context)