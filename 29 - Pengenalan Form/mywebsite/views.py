from django.shortcuts import render

def index(request):
    context = {
        'title': 'Home',
        'heading': 'Home Form',
    }

    if request.method == 'POST':
        print('ini adalah method POST')
        context['nama'] = request.POST['nama']
        context['alamat'] = request.POST['alamat']
    else:
        print('ini adalah method GET')

    return render(request, 'index.html', context)