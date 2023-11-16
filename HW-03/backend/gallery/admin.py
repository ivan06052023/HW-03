from django.contrib import admin

from .models import Gallery, Photo

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    """Галерея"""
    list_display = ("name", "id", "created")
    prepopulated_fields = {"slug": ("name",)}
    ordering = ["id"]
    list_filter = ("name", "created")
    # поиск
    search_fields = ("name", "created")

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    """Фото"""
    list_display = ("name", "id", "created")
    prepopulated_fields = {"slug": ("name",)}
    ordering = ["id"]
    list_filter = ("name", "created")
    search_fields = ("name", "created")