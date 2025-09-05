from django.urls import path
from .views import books_list, books_create, books_edit, books_delete

urlpatterns = [
    path('', books_list, name='books_list'),
    path('new/', books_create, name='books_create'),
    path('edit/<int:pk>/', books_edit, name='books_edit'),
    path('delete/<int:pk>/', books_delete, name='books_delete'),
]

