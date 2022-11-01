from tabnanny import verbose
from django.db import models
from django.shortcuts import reverse

class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name = 'Название')
    slug = models.SlugField(max_length=150, verbose_name='Url для категории', unique=True)

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('products_category', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=250, verbose_name = 'Название')
    description = models.TextField(verbose_name = 'Описание')
    photo = models.ImageField(upload_to='store/photos/', verbose_name = 'Выбрать фото')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = 'Создано')
    updated_at = models.DateTimeField(auto_now = True, verbose_name = 'Изменено')
    is_onsale = models.BooleanField(default=False, verbose_name = 'В продаже')
    views_counter = models.IntegerField(default=0, verbose_name='Количество просмотров')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, 
            verbose_name='Категория', blank=True, null=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('created_at', )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('single_product', kwargs={'pk': self.pk})