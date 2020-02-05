from django.urls import path
from .views import artikelIndexView, artikelAddView, artikelAddView2, otongView

app_name = 'artikel'

urlpatterns = [
    path('otong/', otongView, name='otong'),
    path('add2/', artikelAddView2, name='add2'),
    path('add/', artikelAddView, name='add'),
    path('', artikelIndexView, name='index')
]