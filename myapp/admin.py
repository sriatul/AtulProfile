from django.contrib import admin

# Register your models here.
from .models import atulmodel

@admin.register(atulmodel)

class proAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','email','subject','msg')