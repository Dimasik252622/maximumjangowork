from django.contrib import admin
from .models import Advertisements

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'price', 'create_dated','update_dated','auction']
    list_filter = ['auction', 'created_at']




admin.site.register(Advertisements, AdvertisementAdmin)

# Register your models here.
