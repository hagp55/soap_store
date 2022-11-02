from itertools import product
from django import template
from django.db.models import Count, F
from store.models import Category

register = template.Library()


@register.inclusion_tag('store/include/menu_categories.html')
def show_menu():
    categories = Category.objects.annotate(cnt=Count('products', filter=F('products__is_onsale'))).filter(cnt__gt=0).order_by('order')
    return {'categories': categories}