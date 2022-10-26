from django.shortcuts import render, get_object_or_404
from django.db.models import F
from .models import Product

def index(request):
    products = Product.objects.filter(is_onsale=True).all()
    return render(request, 'store/index.html', {'products': products})

def single_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.views_counter = F('views_counter') + 1
    product.save()
    context = {
        'products' : Product.objects.filter(is_onsale=True).all(),
        'product': product,
    }
    return render(request, 'store/single_product.html', context)


def contact(request):
    return render(request, 'store/contact.html')


