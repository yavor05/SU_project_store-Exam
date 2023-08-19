from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import ProductModel, Cart, CartItem


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'quantity')
    list_filter = ('category', 'price')
    search_fields = ('name', 'description')
    ordering = ('name',)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity')
