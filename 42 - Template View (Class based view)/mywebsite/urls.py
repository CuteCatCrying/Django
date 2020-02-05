"""mywebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import IndexView, ContextView, ParameterView

urlpatterns = [
    path('parameter/<int:parameter1>/<int:parameter2>/', ParameterView.as_view()),
    path('context/', ContextView.as_view()),
    path('default/', IndexView.as_view(template_name='default.html')),
    path('', IndexView.as_view(template_name='index.html')),
    path('admin/', admin.site.urls),
]


'''
    1.  Membuat class view di views.py, tapi meggunaakn templateny di url
    2.  Jika halaman kita itu statis, tidak ada perubahan apapun, 
        maka kita lakukan templateview langsung pada urls.py
    3.  membuat views dengan context saja, kita menggnakan class templatesview di views.py
    4.  Kita memasukan paramter ke dalam template, dengan menggunakan regex
'''