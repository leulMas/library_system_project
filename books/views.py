from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
def books_list(request):
    books = Book.objects.all()
    return render(request, 'books/books_list.html', {'books': books})

def books_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        Book.objects.create(title=title, author=author)
        return redirect('books_list')
    return render(request, 'books/books_form.html')

def books_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.save()
        return redirect('books_list')
    return render(request, 'books/books_form.html', {'book': book})

def books_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('books_list')
