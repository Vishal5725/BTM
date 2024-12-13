from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(FormData)
class FormDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'submited_dateandtime')  