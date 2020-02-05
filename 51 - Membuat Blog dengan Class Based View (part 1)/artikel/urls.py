from django.urls import path
from .views import ArtikelListView, ArtikelDetailView, ArtikelKategoriView

app_name = 'artikel'
urlpatterns = [
    path('kategori/<str:kategori>/<int:page>', ArtikelKategoriView.as_view(), name='category'),
    path('detail/<str:slug>', ArtikelDetailView.as_view(), name='detail'),
    path('<int:page>', ArtikelListView.as_view(), name='list'),
]