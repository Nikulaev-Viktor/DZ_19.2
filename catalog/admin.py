from django.contrib import admin
from catalog.models import Product, Category, Version


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "price", "category", "author")
    list_filter = ("category",)
    search_fields = ("title", "description", "author")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title")


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = (
        "product",
        "version_number",
        "version_name",
        "version_active",
    )
