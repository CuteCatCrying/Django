from django.shortcuts import render

# Create your views here.
def input(request, input):
    context = {
        'Judul': input,
    }
    return render(request, 'blog/index.html', context)

def categoryPost(request):
    context = {
        'Judul': 'Category Post',
    }
    return render(request, 'blog/index.html', context)

def singlePost(request):
    context = {
        'Judul': 'Single Post',
    }
    return render(request, 'blog/index.html', context)

def index(request):
    context = {
        'Judul': 'Home Blog',
    }
    return render(request, 'blog/index.html', context)