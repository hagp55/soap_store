from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=250, verbose_name = 'Название')
    description = models.TextField(blank=True, verbose_name = 'Описание')
    photo = models.ImageField(upload_to='store/photos/', verbose_name = 'Выбрать фото')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = 'Создано')
    updated_at = models.DateTimeField(auto_now = True, verbose_name = 'Изменено')
    is_onsale = models.BooleanField(default=False, verbose_name = 'В продаже')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('created_at', )

    def __str__(self):
        return self.title

