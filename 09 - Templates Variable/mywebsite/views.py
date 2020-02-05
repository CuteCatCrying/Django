from django.shortcuts import render

def index(request):
    context = {
        'judul':'Kelas Terbuka',
        'kontributor':'Zukron Alviandy R'
    }
    return render(request, 'index.html', context)