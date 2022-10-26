# Generated by Django 4.1.2 on 2022-10-25 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_category_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='views_counter',
            field=models.IntegerField(default=0, verbose_name='Количество просмотров'),
        ),
    ]