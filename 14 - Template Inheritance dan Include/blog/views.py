from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title': 'Blog',
        'heading': 'Blog',
        'subheading': 'Jurnal Kelas Terbuka'
    }
    return render(request, 'blog/index.html', context)