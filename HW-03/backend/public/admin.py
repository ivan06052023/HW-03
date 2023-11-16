from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import Coords, Level, FilterPereval, Pereval_added

@admin.register(Coords)
class CoordsAdmin(admin.ModelAdmin):
    """Координаты"""
    list_display = ("id", "latitude", "longitude", "height")
    list_display_links = ("id",)
    ordering = ["id"]
    list_filter = ("id", "latitude", "longitude", "height")
    # поиск
    search_fields = ("id", "latitude", "longitude", "height")

@admin.register(Level)
class LevelAdmin(MPTTModelAdmin):
    """сложность перевала"""
    list_display = ("name", "parent", "id")
    mptt_level_indent = 20
    prepopulated_fields = {"slug":("name",)}
    list_filter = ("name", "parent")
    # поиск
    search_fields = ("name", "parent")

@admin.register(FilterPereval)
class FilterPerevalAdmin(admin.ModelAdmin):
    """фильтры"""
    list_display = ("name", "id")
    list_display_links = ("name",)
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Pereval_added)
class Pereval_addedAdmin(admin.ModelAdmin):
    """Новое название"""
    list_display = (
        "id",
        "beautyTitle",
        "title",
        "other_titles",
        "user",
        "filters",
        "slug",
    )
    list_display_links = ("beautyTitle",)

    list_filter = (
        "beautyTitle",
        "title",
        "other_titles",
        "user",
        "filters",
    )
    prepopulated_fields = {"slug": ("user", "beautyTitle")}
    ordering = ["id"]
    # поиск
    search_fields = ("beautyTitle", "user", "title" )