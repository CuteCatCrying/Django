from django.shortcuts import render

def index(request):
    context = {
        'Judul': 'Home',
    }
    return render(request, 'index.html', context)