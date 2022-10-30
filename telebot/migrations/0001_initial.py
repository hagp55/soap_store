# Generated by Django 4.1.2 on 2022-10-30 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeleBotSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_token', models.CharField(max_length=200, verbose_name='Телеграм токен')),
                ('telegram_chat_id', models.CharField(max_length=200, verbose_name='Телеграм чат айди')),
                ('telegram_message', models.TextField(verbose_name='Текст сообщения')),
            ],
            options={
                'verbose_name': 'настройку',
                'verbose_name_plural': 'Настройки',
            },
        ),
    ]
