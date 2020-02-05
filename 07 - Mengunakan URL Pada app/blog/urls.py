from django.urls import path
from . import views

urlpatterns = [
    path('recent/', views.recent),
    path('', views.index),
]