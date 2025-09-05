# checkout/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Checkout
from .serializers import CheckoutSerializer
from books.models import Book
from users.models import User

# -------------------------------
# API ViewSet
# -------------------------------
class CheckoutViewSet(viewsets.ModelViewSet):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer

    @action(detail=True, methods=['post'])
    def return_book(self, request, pk=None):
        checkout = self.get_object()
        checkout.return_date = timezone.now()
        checkout.save()
        return Response({'status': 'book returned'})

# -------------------------------
# Frontend Views
# -------------------------------
def checkout_list(request):
    checkouts = Checkout.objects.all()
    return render(request, 'checkout_list.html', {'checkouts': checkouts})

def checkout_create(request):
    users = User.objects.all()
    books = Book.objects.all()

    if request.method == 'POST':
        user_id = request.POST.get('user')
        book_id = request.POST.get('book')
        checkout_date = request.POST.get('checkout_date')
        return_date = request.POST.get('return_date')

        Checkout.objects.create(
            user=User.objects.get(pk=user_id),
            book=Book.objects.get(pk=book_id),
            checkout_date=checkout_date,
            return_date=return_date
        )
        return redirect('checkout_list')

    return render(request, 'checkout_form.html', {'users': users, 'books': books})

def checkout_edit(request, pk):
    checkout = get_object_or_404(Checkout, pk=pk)
    users = User.objects.all()
    books = Book.objects.all()

    if request.method == 'POST':
        checkout.user = User.objects.get(pk=request.POST.get('user'))
        checkout.book = Book.objects.get(pk=request.POST.get('book'))
        checkout.checkout_date = request.POST.get('checkout_date')
        checkout.return_date = request.POST.get('return_date')
        checkout.save()
        return redirect('checkout_list')

    return render(request, 'checkout_form.html', {'checkout': checkout, 'users': users, 'books': books})

def checkout_delete(request, pk):
    checkout = get_object_or_404(Checkout, pk=pk)
    checkout.delete()
    return redirect('checkout_list')
