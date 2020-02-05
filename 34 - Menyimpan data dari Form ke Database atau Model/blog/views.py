from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import PostForm
from .models import PostModel
# Create your views here.

def index(request):
    posts = PostModel.objects.all()

    context = {
        'page_title': 'List Post',
        'posts': posts,
    }
    return render(request, 'blog/index.html', context)

def create(request):
    post_form = PostForm()

    if request.method == 'POST':
        PostModel.objects.create(
            # judul=request.POST['judul'],
            # body=request.POST['body'],
            # category=request.POST['category'],
            judul= request.POST.get('judul'),
            body= request.POST.get('body'),
            category= request.POST.get('category'),
        )

        return HttpResponseRedirect('/blog/')

    context = {
        'page_title': 'Create Post',
        'post_form': post_form,
    }

    return render(request, 'blog/create.html', context)