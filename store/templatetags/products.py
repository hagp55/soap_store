from django import template
from store.models import Product

register = template.Library()


@register.simple_tag
def get_new_product():
    return Product.objects.order_by('-created_at')[:10]


