from django.contrib import admin
from .models import Office


@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'address', 'latitude', 'longitude')
    search_fields = ('name', 'city__name', 'address')
    list_filter = ('city',)
    autocomplete_fields = ("city",)
