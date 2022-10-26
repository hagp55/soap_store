# Generated by Django 4.1.2 on 2022-10-25 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_is_onsale'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('created_at',), 'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
        migrations.AddField(
            model_name='product',
            name='views_counter',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Создано'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_onsale',
            field=models.BooleanField(default=False, verbose_name='В продаже'),
        ),
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(upload_to='store/photos/', verbose_name='Выбрать фото'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=250, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Изменено'),
        ),
    ]