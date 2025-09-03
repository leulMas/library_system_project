from django.contrib import admin
from .models import Checkout

@admin.register(Checkout)
class CheckoutAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'checkout_date', 'return_date')
    search_fields = ('user_username','book_title')
    list_filter = ('checkout_date', 'return_date')
    
