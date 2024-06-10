from django.contrib import admin
from .models import CustomUser, Category, Crypto, CustomGroup

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    fields = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'type', "groups",]
    list_display = ("username", "email", "first_name", "is_staff", "type",  )
    list_filter = ("is_staff", "groups", "type")
    list_editable = ('type', )
    filter_horizontal = ("groups", "user_permissions",)
@admin.register(CustomGroup)
class CustomGroupAdmin(admin.ModelAdmin):
    search_fields = ("Название группы",)
    ordering = ("name",)
    filter_horizontal = ("permissions",)

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        if db_field.name == "permissions":
            qs = kwargs.get("queryset", db_field.remote_field.model.objects)
            kwargs["queryset"] = qs.select_related("content_type")
        return super().formfield_for_manytomany(db_field, request=request, **kwargs)
@admin.register(Crypto)
class CryptoAdmin(admin.ModelAdmin):
    fields = ['title', 'category', 'user', 'content', 'is_published', 'groups']
    list_display = ('title', 'category', 'user', 'is_published')
    # list_display_links = ('username',)
    list_editable = ('is_published',)

@admin.register(Category)
class CryptoAdmin(admin.ModelAdmin):
    fields = ['name', 'slug']
    list_display = ('name', 'slug')


# admin.site.register(CustomUser)



