from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Box)
class FilterBox(admin.ModelAdmin):
    list_display = ('category', 'location')  