from django.db import models
from django.utils.html import format_html

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField(null=True, blank=True)  # New field
    total_copies = models.PositiveIntegerField(default=1)
    available_copies = models.PositiveIntegerField(default=1)

    def is_available(self):
        """Check if book is available based on available_copies"""
        return self.available_copies > 0

    is_available.boolean = True   # Shows as ✔/✘ in admin list
    is_available.short_description = "Available"  # Column header in admin

    def availability_status(self):
        """Pretty colored label for availability"""
        if self.available_copies > 0:
            return format_html('<span style="color: green;">✔ In Stock</span>')
        return format_html('<span style="color: red;">✘ Out of Stock</span>')

    availability_status.short_description = "Status"

    def __str__(self):
        return f"{self.title} by {self.author}"
