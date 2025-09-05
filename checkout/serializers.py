from rest_framework import serializers
from .models import Checkout
from users.models import User
from books.models import Book
from users.serializers import UserSerializer
from books.serializers import BookSerializer

class CheckoutSerializer(serializers.ModelSerializer):
    # Nested serializers for GET responses
    user_details = UserSerializer(source='user', read_only=True)
    book_details = BookSerializer(source='book', read_only=True)
    
    # SlugRelatedFields for nicer dropdowns in browsable API and POST/PUT
    user = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field='username'
    )
    book = serializers.SlugRelatedField(
        queryset=Book.objects.all(), slug_field='title'
    )
    
    class Meta:
        model = Checkout
        fields = ['id', 'user', 'user_details', 'book', 'book_details', 'checkout_date', 'return_date']
