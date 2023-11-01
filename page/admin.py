from django.contrib import admin

# Register your models here.

from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'name', 'date_registered', 'phone_number', 'is_staff']

admin.site.register(CustomUser, CustomUserAdmin)
