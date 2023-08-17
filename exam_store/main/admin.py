from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import ProductModel


class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'quantity')
    list_filter = ('category',)
    search_fields = ('name', 'description')
    ordering = ('name',)


admin.site.register(ProductModel, ProductModelAdmin)
