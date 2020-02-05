from django.shortcuts import render, redirect

# Create your views here.
from .forms import PostForm
from .models import Post

def index(request):
    posts = Post.objects.all()
    context = {
        'page_title': 'Post List',
        'posts': posts
    }

    return render(request, 'blog/index.html', context)

def create(request):
    post_from = PostForm(request.POST or None)

    if request.method == 'POST':
        if post_from.is_valid():
            post_from.save()
            # Post.objects.create(
            #     judul=request.POST.get('judul'),
            #     body=request.POST.get('body'),
            #     category=request.POST.get('category'),
            # )
            
            return redirect('blog:index')
    
    context = {
        'page_title': 'Create Post',
        'post_form': post_from,
    }
    return render(request, 'blog/create.html', context)