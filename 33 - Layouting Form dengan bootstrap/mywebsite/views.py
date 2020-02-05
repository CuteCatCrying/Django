from django.shortcuts import render

def index(request):
    context = {
        'heading': 'Home',
        'content': 'Ini adalah home',
    }
    return render(request, 'index.html', context)