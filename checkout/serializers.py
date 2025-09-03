from rest_framework import serializers
from .models import Checkout
from users.serializers import UserSerializer
from books.serializers import BookSerializer

class CheckoutSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=Checkout.objects.all())
    book = serializers.PrimaryKeyRelatedField(queryset=Checkout.objects.all())
    
    class Meta:
        model = Checkout
        fields = ['id', 'user', 'book', 'checkout_date', 'return_date']
