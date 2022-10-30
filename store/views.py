from django.shortcuts import render, get_object_or_404
from django.db.models import F
from .models import Product
from telebot.send_message import send_telegram
from telebot.forms import TeleBotSendMessageForm


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