from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<str:categoryInput>/', views.categoryPost),
    path('post/<str:slugInput>', views.singlePost)
]