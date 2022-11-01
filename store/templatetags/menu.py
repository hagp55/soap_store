from django import template
from store.models import Category

register = template.Library()


@register.inclusion_tag('store/include/navbar_menu.html')
def show_menu():
    categories = Category.objects.all()
    return {'categories': categories}