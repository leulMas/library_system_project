from django.urls import path
from .views import checkout_list, checkout_create, checkout_edit, checkout_delete, checkout_return

urlpatterns = [
    path('', checkout_list, name='checkout_list'),
    path('new/', checkout_create, name='checkout_create'),
    path('edit/<int:pk>/', checkout_edit, name='checkout_edit'),
    path('delete/<int:pk>/', checkout_delete, name='checkout_delete'),
    path('return/<int:pk>/', checkout_return, name='checkout_return'),
]
