from django.contrib import admin
from products.models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'received_on', 'supplier_name')
    fields = ('name', 'supplier_name', ('price', 'measure',), 'received_on',)
    readonly_fields = ('received_on',)
    ordering = ('name', 'supplier_name',)
    search_fields = ('name',)
