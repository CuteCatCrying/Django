from django.urls import path
from django.views.generic import ListView
from .views import index, ArtikelListView
from .models import Artikel

app_name = 'blog'
urlpatterns = [
    path('<str:penulis>/<int:page>', ArtikelListView.as_view(), name='list'),
    # path('', ListView.as_view(model=Artikel), name='list'),
]