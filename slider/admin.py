from django.contrib import admin
from django import forms
from .models import Slider
from django.utils.safestring import mark_safe
from ckeditor.widgets import CKEditorWidget


class SliderAdminForm(forms.ModelForm):
    title = forms.CharField(widget=CKEditorWidget())
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Slider
        fields = '__all__'


class SliderAdmin(admin.ModelAdmin):
    form = SliderAdminForm
    fields = ('title', 'content', 'get_photo', 'photo', 'price')
    readonly_fields = ('get_photo',)

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="500px">')
        else:
            return 'Фото отсуствует'

    get_photo.short_description = 'Фото'

admin.site.register(Slider, SliderAdmin)