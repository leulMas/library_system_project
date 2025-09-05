from django.urls import path
from .views import users_list, users_create, users_edit, users_delete

urlpatterns = [
    path('', users_list, name='users_list'),
    path('new/', users_create, name='users_create'),
    path('edit/<int:pk>/', users_edit, name='users_edit'),
    path('delete/<int:pk>/', users_delete, name='users_delete'),
]
