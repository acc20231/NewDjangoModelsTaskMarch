from django.contrib import admin
from django.contrib.auth import authenticate
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Category, Crypto

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    fields = ['username', 'email', 'is_staff', 'is_active', 'is_superuser', 'type']
    list_display = ('username', 'is_staff','is_active', 'is_superuser', 'type')
    list_display_links = ('username',)
    list_editable = ('type',)


admin.site.register(Category)
admin.site.register(Crypto)