from django.contrib import admin
from .models import Product
from django.utils.safestring import mark_safe


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'is_onsale', 'get_preview_photo')
    list_editable = ('is_onsale', )
    search_fields = ('title', 'description')
    fields = ('title', 'description', 'get_photo', 'photo', 'is_onsale')
    readonly_fields = ('get_photo', )

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="200px">')
        else:
            return 'Фото отсуствует'

    
    def get_preview_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50px">')
        else:
            return 'Фото отсуствует'


    get_preview_photo.short_description = 'Миниатюра'
    get_photo.short_description = 'Фото'

admin.site.register(Product, ProductAdmin)
admin.site.site_title = 'Админка chlenomylo'
admin.site.site_header = 'Chlenomylo'