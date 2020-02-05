from django.http import HttpResponse

# method view
def index(request):
    judul = '<h1>Ini adalah home</h1>'
    subjudul = '<h2>Selamat datang di website ini</h2>'

    output = judul + subjudul
    return HttpResponse(output)

def about(request):
    return HttpResponse('<h1>Ini adalah About</h1>')