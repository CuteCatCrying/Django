from django.urls import path
from . import views

# app_name = 'blog'

urlpatterns = [
    path('khusus/<str:input>/', views.input, name='khusus'),
    path('category/', views.categoryPost, name='category'),
    path('single/', views.singlePost, name='single'),
    path('', views.index, name='index'),
]