from django.shortcuts import render
from django.views import View

def index(request):
    context = {
        'heading': 'Selamat Datang'
    }

    if request.method == 'POST':
        context['heading'] = 'POST Function Based View'

    return render(request, 'index.html', context)


class IndexClassView(View):
    template_name = ''
    context = {}
    # override method get dari parent class view
    def get(self, request):
        self.context['heading'] = 'GET Class Based View'
        return render(request, self.template_name, self.context)

    def post(self, request):
        self.context['heading'] = 'POST Class Based View'
        return render(request, self.template_name, self.context)