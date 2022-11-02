# Generated by Django 4.1.2 on 2022-11-02 04:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='order',
            field=models.IntegerField(blank=True, null=True, verbose_name='Порядок меню'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='products', to='store.category', verbose_name='Категория'),
        ),
    ]
