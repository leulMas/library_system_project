from django.db import models
from users.models import User
from books.models import Book
from django.core.exceptions import ValidationError
from django.utils import timezone

class Checkout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="checkouts")
    book = models.ForeignKey('books.Book', on_delete=models.CASCADE, related_name="checkouts")  # Use string reference
    checkout_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)

    def clean(self):
        """Ensure return date is not before checkout date"""
        if self.return_date and self.return_date < self.checkout_date:
            raise ValidationError("Return date cannot be before the checkout date.")

    def save(self, *args, **kwargs):
        # Run validation before saving
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user} → {self.book}"
