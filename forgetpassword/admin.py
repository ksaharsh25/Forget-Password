from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display=['email','password']