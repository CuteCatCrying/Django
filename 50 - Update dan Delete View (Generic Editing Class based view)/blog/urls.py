from django.urls import path
from django.views.generic import ListView, DetailView, FormView
from .views import ArtikelListView, ArtikelDetailView, ArtikelFormView, ArtikelCreateView1, ArtikelCreateView2, ArtikelUpdateView1, ArtikelUpdateView2, ArtikelDeleteView
from .models import Artikel
from .forms import ArtikelForm

app_name = 'blog'
urlpatterns = [
    path('delete/<int:pk>', ArtikelDeleteView.as_view(), name='delete'),
    path('update2/<int:pk>', ArtikelUpdateView2.as_view(), name='update2'),
    path('update1/<int:pk>', ArtikelUpdateView1.as_view(), name='update1'),
    path('create/', ArtikelCreateView2.as_view(), name='create'),
    # path('create/', ArtikelCreateView1.as_view(), name='create'),
    # path('create/', ArtikelFormView.as_view(), name='create'),
    # path('create/', FormView.as_view(form_class=ArtikelForm, template_name='blog/create.html'), name='create'),
    path('<str:penulis>/<int:page>', ArtikelListView.as_view(), name='list'),
    path('<str:penulis>/', ArtikelListView.as_view(), name='list'),
    path('detail/<str:slug>/', ArtikelDetailView.as_view(model=Artikel), name='detail'),
    # path('detail/<str:slug>/', DetailView.as_view(model=Artikel), name='detail'),
    # path('', ListView.as_view(model=Artikel), name='list'),
]