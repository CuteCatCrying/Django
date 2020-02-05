from django.urls import path
from django.views.generic import ListView, DetailView
from .views import ArtikelListView, ArtikelDetailView
from .models import Artikel

app_name = 'blog'
urlpatterns = [
    path('<str:penulis>/<int:page>', ArtikelListView.as_view(), name='list'),
    path('<str:penulis>/', ArtikelListView.as_view(), name='list'),
    path('detail/<str:slug>/', ArtikelDetailView.as_view(model=Artikel), name='detail'),
    # path('detail/<str:slug>/', DetailView.as_view(model=Artikel), name='detail'),
    # path('', ListView.as_view(model=Artikel), name='list'),
]