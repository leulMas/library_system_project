from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib import messages
from django.utils.dateparse import parse_datetime
from django.contrib.auth.decorators import login_required

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

        # Increase available copies when book is returned
        book = checkout.book
        book.available_copies += 1
        book.save()

        return Response({'status': 'book returned'})


# -------------------------------
# Frontend Views
# -------------------------------

@login_required
def checkout_list(request):
    checkouts = Checkout.objects.select_related('book', 'user').all()
    return render(request, 'checkout_list.html', {'checkouts': checkouts})


@login_required
def checkout_create(request):
    users = User.objects.all()
    books = Book.objects.filter(available_copies__gt=0)  # Only allow books with stock

    if request.method == 'POST':
        user_id = request.POST.get('user')
        book_id = request.POST.get('book')
        checkout_date = request.POST.get('checkout_date')
        return_date = request.POST.get('return_date')

        # Parse datetime strings
        checkout_dt = parse_datetime(checkout_date) if checkout_date else None
        return_dt = parse_datetime(return_date) if return_date else None

        # Validate return date
        if return_dt and checkout_dt and return_dt < checkout_dt:
            messages.error(request, "Return date cannot be before checkout date!")
            return render(request, 'checkout_form.html', {'users': users, 'books': books})

        book = Book.objects.get(pk=book_id)

        if book.available_copies <= 0:
            messages.error(request, "Cannot checkout. Book is out of stock!")
            return render(request, 'checkout_form.html', {'users': users, 'books': books})

        # Create checkout
        Checkout.objects.create(
            user=User.objects.get(pk=user_id),
            book=book,
            checkout_date=checkout_date,
            return_date=return_date
        )

        # Decrease available copies
        book.available_copies -= 1
        book.save()

        messages.success(request, "Book checked out successfully!")
        return redirect('checkout_list')

    return render(request, 'checkout_form.html', {'users': users, 'books': books})


@login_required
def checkout_edit(request, pk):
    checkout = get_object_or_404(Checkout, pk=pk)
    users = User.objects.all()
    books = Book.objects.all()

    if request.method == 'POST':
        user = User.objects.get(pk=request.POST.get('user'))
        book = Book.objects.get(pk=request.POST.get('book'))
        checkout_date = request.POST.get('checkout_date')
        return_date = request.POST.get('return_date')

        # Parse datetime strings
        checkout_dt = parse_datetime(checkout_date) if checkout_date else None
        return_dt = parse_datetime(return_date) if return_date else None

        # Validate return date
        if return_dt and checkout_dt and return_dt < checkout_dt:
            messages.error(request, "Return date cannot be before checkout date!")
            return render(request, 'checkout_form.html', {
                'checkout': checkout,
                'users': users,
                'books': books
            })

        # If book changed, adjust stock
        if checkout.book != book:
            # Increase stock of old book
            old_book = checkout.book
            old_book.available_copies += 1
            old_book.save()

            # Decrease stock of new book if available
            if book.available_copies <= 0:
                messages.error(request, "Cannot assign this book. Out of stock!")
                return render(request, 'checkout_form.html', {
                    'checkout': checkout,
                    'users': users,
                    'books': books
                })
            book.available_copies -= 1
            book.save()

        # Update checkout
        checkout.user = user
        checkout.book = book
        checkout.checkout_date = checkout_date
        checkout.return_date = return_date
        checkout.save()

        messages.success(request, "Checkout updated successfully!")
        return redirect('checkout_list')

    return render(request, 'checkout_form.html', {'checkout': checkout, 'users': users, 'books': books})


@login_required
def checkout_delete(request, pk):
    checkout = get_object_or_404(Checkout, pk=pk)

    if request.method == 'POST':
        # Restore book stock when deleting checkout
        book = checkout.book
        book.available_copies += 1
        book.save()

        checkout.delete()
        messages.success(request, "Checkout deleted successfully!")
        return redirect('checkout_list')

    return render(request, 'checkout/checkout_confirm_delete.html', {'checkout': checkout})


@login_required
def checkout_return(request, pk):
    checkout = get_object_or_404(Checkout, pk=pk)

    if request.method == "POST":
        book = checkout.book
        book.available_copies += 1
        book.save()

        checkout.delete()

        messages.success(request, f"You have successfully returned '{book.title}'.")
        return redirect("checkout_list")

    return render(request, "checkout/checkout_confirm_return.html", {"checkout": checkout})
