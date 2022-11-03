from django.db import models


class Slider(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Текст')
    photo = models.ImageField(upload_to='slider/photos/', verbose_name='Выбрать картинку')
    price = models.IntegerField(null=True, blank=True, verbose_name='Цена')

    def __str__(self):
        return f'Слайдер № {self.pk}'

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'
        ordering = ('pk',)