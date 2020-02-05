from django.shortcuts import render

# Create your views here.
from .forms import ContactForm

def index(request):
    contact_form = ContactForm()
    context = {
        'heading': 'Contact',
        'data_form': contact_form,
    }

    print(request.POST)
    return render(request, 'index.html', context)