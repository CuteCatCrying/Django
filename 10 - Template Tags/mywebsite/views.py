from django.shortcuts import render

def index(request):
    context = {
        'judul':'Kelas Terbuka',
        'subjudul':'Selamat Datang',
        'nav': [
            ['/' , 'Home'],
            ['/blog', 'Blog'],
            ['/about', 'About'],
            ['/contact', 'Contact']
        ]
    }
    return render(request, 'index.html', context)