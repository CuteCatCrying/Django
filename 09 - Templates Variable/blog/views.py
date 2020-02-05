from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'judul':'Blog',
        'kontributor':'Ucup'
    }
    return render(request, 'blog/index.html', context)

def news(request):
    context = {
        'judul':'News',
        'kontributor':'Burhan'
    }
    return render(request, 'blog/index.html', context)

def cerita(request):
    context = {
        'judul':'Cerita',
        'kontributor':'Sandra'
    }
    return render(request, 'blog/index.html', context)