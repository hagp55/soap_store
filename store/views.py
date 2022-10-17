from django.shortcuts import render
from .models import Product

def index(request):
    products = Product.objects.filter(is_onsale=True).all()
    return render(request, 'store/index.html', {'products': products})


def about_us(request):
    return render(request, 'store/about.html')


def contact(request):
    return render(request, 'store/contact.html')

def basic(request):
    return render(request, 'base.html')