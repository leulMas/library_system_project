from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from users.views import UserViewSet
from books.views import BookViewSet
from checkout.views import CheckoutViewSet
from django.http import HttpResponse
from django.shortcuts import render
from users import views as user_views


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'books', BookViewSet)
router.register(r'checkout', CheckoutViewSet)

def home(request):
    return render(request,"home.html")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("signup/", user_views.signup, name="signup"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("api/", include(router.urls)),       # API endpoints
    path("users/", include("users.urls")),    # Users frontend
    path("books/", include("books.urls")),    # Books frontend
    path("checkout/", include("checkout.urls")),  # Checkout frontend
    path("", home, name="home")
]


