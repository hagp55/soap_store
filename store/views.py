from multiprocessing import context
from unicodedata import category
from django.shortcuts import render, get_object_or_404
from django.db.models import F
from .models import Product, Category
from telebot.send_message import send_telegram
from telebot.forms import TeleBotSendMessageForm
from django.views.generic import ListView


def index(request):
    products = Product.objects.filter(is_onsale=True).all()
    categories = Category.objects.all()
    context = {
        'products': products,
        'categories': categories,
        }
    return render(request, 'store/index.html', context)


class ProductsByCategoryView(ListView):
    template_name = 'store/category.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['slug'])

# def products_by_category(request, slug):
#     products = Category.objects.get(slug=slug)
#     print(products)
#     context = {
#         'products': products,
#     }
#     return render(request, 'store/category.html', context)    




def single_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.views_counter = F('views_counter') + 1
    product.save()
    context = {
        'products' : Product.objects.filter(is_onsale=True).all(),
        'product': product,
    }
    return render(request, 'store/single_product.html', context)


def all_products(request):
    products = Product.objects.filter(is_onsale=True).all()
    return render(request, 'store/category.html', {'products': products})



def contact(request):
    if request.method == 'POST':
        form = TeleBotSendMessageForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone']
            # email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            send_telegram(phone, message)
        else:
            print('Not OK')
    form = TeleBotSendMessageForm()
    return render(request, 'store/contact.html', {'form': form})


def page_not_found(request):
    return render(request, '404.html')