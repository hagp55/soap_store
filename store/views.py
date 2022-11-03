from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.db.models import F
from django.contrib import messages

from .models import Product, Category, Tag
from slider.models import Slider
from telebot.forms import TeleBotSendMessageForm
from telebot.send_message import send_telegram


class HomeView(ListView):
    template_name = 'store/index.html'
    context_object_name = 'products'
    paginate_by = 18

    def get_queryset(self):
        return Product.objects.filter(is_onsale=True).all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sliders'] = Slider.objects.all()
        context['categories'] = Category.objects.all()
        return context


class ProductsByCategoryView(ListView):
    template_name = 'store/category.html'
    context_object_name = 'products'
    allow_empty = False
    paginate_by = 18

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['slug'], is_onsale=True)

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     context['title'] = Category.objects.get(slug=self.kwargs['slug'])
    #     return context


class ProductsByTagsView(ListView):
    template_name = 'store/category.html'
    context_object_name = 'products'
    allow_empty = False
    paginate_by = 18

    def get_queryset(self):
        return Product.objects.filter(tags__slug=self.kwargs['slug'], is_onsale=True)

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     context['title'] = f'{Tag.objects.get(slug=self.kwargs["slug"])}'
    #     return context


class SingleProducDetailView(DetailView):
    model = Product
    template_name = 'store/single_product.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(is_onsale=True).all()
        self.object.views_counter = F('views_counter') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context


def contact(request):
    if request.method == 'POST':
        form = TeleBotSendMessageForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            send_telegram(request, phone, message)                
        else:
            messages.error(request, 'Заполните все поля')
    form = TeleBotSendMessageForm()
    return render(request, 'store/contact.html', {'form': form})
