from django.urls import path
from django.contrib.auth import views as auth_views
from .views import users_list, users_create, users_edit, users_delete
from . import views

urlpatterns = [
    path('', users_list, name='users_list'),
    path('new/', users_create, name='users_create'),
    path('edit/<int:pk>/', users_edit, name='users_edit'),
    path('delete/<int:pk>/', users_delete, name='users_delete'),
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),

]
