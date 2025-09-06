from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets

# REST API viewset
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# List all books
def books_list(request):
    books = Book.objects.all()
    return render(request, 'books/books_list.html', {'books': books})

# Create a new book
def books_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        published_date = request.POST['published_date']
        total_copies = int(request.POST.get('total_copies', 1))

        Book.objects.create(
            title=title,
            author=author,
            published_date=published_date,
            total_copies=total_copies,
            available_copies=total_copies  # all copies initially available
        )
        return redirect('books_list')

    return render(request, 'books/books_form.html')

# Edit an existing book
def books_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.published_date = request.POST['published_date']
        total_copies = int(request.POST.get('total_copies', book.total_copies))

        # Adjust available copies if total copies changed
        difference = total_copies - book.total_copies
        book.total_copies = total_copies
        book.available_copies = max(0, book.available_copies + difference)

        book.save()
        return redirect('books_list')

    return render(request, 'books/books_form.html', {'book': book})

# Delete a book
def books_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('books_list')
