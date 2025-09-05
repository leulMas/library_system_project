from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Checkout
from .serializers import CheckoutSerializer
from books.models import Book
from users.models import User
from rest_framework.decorators import action

class CheckoutViewSet(viewsets.ModelViewSet):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer
    
    @action(detail=True, methods=['post'])
    def return_book(self, request, pk=None):
        checkout = self.get_object()
        checkout.return_date = timezone.now()
        checkout.save()
        return Response({'status': 'book returned'})
