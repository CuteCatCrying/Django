from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('post/<str:slugInput>', views.detailPost),
    path('category/<str:categoryInput>', views.categoryPost),
]