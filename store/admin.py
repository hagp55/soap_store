from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_onsale')
    list_editable = ('is_onsale', )

admin.site.register(Product, ProductAdmin)