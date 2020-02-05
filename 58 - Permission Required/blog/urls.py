from django.urls import path
from .views import indexView, addView, updateView

app_name = 'blog'
urlpatterns = [
    path('update/', updateView, name='update'),
    path('add/', addView, name='add'),
    path('', indexView, name='index'),
]