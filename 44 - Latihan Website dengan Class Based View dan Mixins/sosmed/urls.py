from django.urls import path

from .views import (
    SosmedListView,
    SosmedDeleteView,
    SosmedFormView,
    )

app_name = 'sosmed'
urlpatterns = [
    path('delete/<int:delete_id>', SosmedDeleteView.as_view(), name='delete'),
    path('update/<int:update_id>', SosmedFormView.as_view(mode='update'), name='update'),
    path('create/', SosmedFormView.as_view(), name='create'),
    path('', SosmedListView.as_view(), name='list')
]