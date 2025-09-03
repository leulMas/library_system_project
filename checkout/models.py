from django.db import models
from users.models import User
from books.models import Book

class Checkout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="checkouts")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="checkouts")
    checkout_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)
    
    def _str_(self):
        return f"{self.user} → {self.book}"
    
