from django.contrib import admin
from django.contrib.auth import authenticate
from django.contrib.auth.admin import UserAdmin
# from .forms import CustomUserCreationForm
from .models import CustomUser, Category, Crypto


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    fields = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'type']
    list_display = ('username', 'is_staff', 'is_superuser', 'type')
    # list_display_links = ('username',)
    list_editable = ('type',)

@admin.register(Crypto)
class CryptoAdmin(admin.ModelAdmin):
    fields = ['title', 'category', 'user', 'content', 'is_published']
    list_display = ('title', 'category', 'user', 'is_published')
    # list_display_links = ('username',)
    list_editable = ('is_published',)


admin.site.register(Category)