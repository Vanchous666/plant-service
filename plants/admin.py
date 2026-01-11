from django.contrib import admin
from .models import Plant

@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'watering_frequency', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('name', 'latin_name', 'description')