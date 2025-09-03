from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from users.views import UserViewSet
from books.views import BookViewSet
from checkout.views import CheckoutViewSet
from django.http import HttpResponse

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'books', BookViewSet)
router.register(r'checkout', CheckoutViewSet)

def home(request):
    return HttpResponse("<h1>📚 Welcome to the Library System API</h1><p>Use <a href='/api/'>/api/</a> to explore endpoints.</p>")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("", home),
]

