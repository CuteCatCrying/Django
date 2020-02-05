from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('post/<str:slugInput>', views.detailPost),
]