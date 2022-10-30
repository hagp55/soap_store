from django.db import models


class TeleBotSettings(models.Model):
    telegram_token = models.CharField(max_length=200, verbose_name='Телеграм токен')
    telegram_chat_id = models.CharField(max_length=200, verbose_name='Телеграм чат айди')
    telegram_message = models.TextField(verbose_name='Макет сообщения')


    class Meta:
        verbose_name = 'настройку'
        verbose_name_plural = 'Настройки'

    def __str__(self):
        return f'Настройки телеграм бота. Не трогать!'
        
        
        
        