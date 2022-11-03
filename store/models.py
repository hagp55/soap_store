from django.db import models
from django.shortcuts import reverse


class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name = 'Название')
    slug = models.SlugField(max_length=150, verbose_name='Url для категории', unique=True, db_index=True)
    order = models.IntegerField(verbose_name='Порядок меню', blank=True, null=True)

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'
        ordering = ('order',)

    def get_absolute_url(self):
        return reverse('products_category', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=50, verbose_name='Тэг')
    slug = models.SlugField(max_length=50, verbose_name='Url для тэга', unique=True, db_index=True)

    class Meta:
        verbose_name = 'тэг'
        verbose_name_plural = 'Тэги'
        ordering = ('title',)

    def get_absolute_url(self):
        return reverse('products_tag', kwargs={'slug': self.slug})

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
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Цена', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, 
                                blank=True, null=True, 
                                verbose_name='Категория', related_name='products')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='Тэг', related_name='products',)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('created_at', )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('single_product', kwargs={'pk': self.pk})