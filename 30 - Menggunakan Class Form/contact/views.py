from django.shortcuts import render
from .forms import ContactForm
# Create your views here.

def index(request):
    contact_form = ContactForm()

    context = {
        'title': 'Contact',
        'heading': 'Contact Form',
        'contact_form': contact_form
    }

    if request.method == 'POST':
        context['nama'] = request.POST['nama']
        context['alamat'] = request.POST['alamat']
    return render(request, 'contact/index.html', context)