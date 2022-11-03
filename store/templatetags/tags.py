from django import template
from store.models import Tag
from django.db.models import Count, F, Sum

register = template.Library()


@register.inclusion_tag('store/include/tags.html')
def get_tags():
    # tags = Tag.objects.annotate(
    #     cnt_onsale=Count('products', filter=F('products__is_onsale'))).annotate(
    #     cnt_sum_views=Sum('products__views_counter')
    #     ).filter(cnt_onsale__gt=0).order_by('-cnt_sum_views')
    

    tags = Tag.objects.annotate(
        cnt_onsale=Count('products', filter=F('products__is_onsale'))).filter(cnt_onsale__gt=0).order_by('-cnt_onsale')
    # for tag in tags:
    #     print(tag.title, tag.products.all()[0].views_counter)
    return {"tags": tags}