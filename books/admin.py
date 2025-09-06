from django.contrib import admin
from .models import Book


class AvailabilityFilter(admin.SimpleListFilter):
    title = 'Availability'
    parameter_name = 'availability'

    def lookups(self, request, model_admin):
        return (
            ('available', 'Available'),
            ('unavailable', 'Out of stock'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'available':
            return queryset.filter(available_copies__gt=0)
        if self.value() == 'unavailable':
            return queryset.filter(available_copies=0)


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'total_copies', 'available_copies', 'is_available')
    list_filter = (AvailabilityFilter,)


# Register the model with admin
admin.site.register(Book, BookAdmin)
