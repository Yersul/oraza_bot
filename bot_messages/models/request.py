from operator import mod
from statistics import mode
from django.db import models
from django.utils.translation import gettext_lazy as _

from bot_messages.models.action import Action


class Request(models.Model):
    # user = models.ForeignKey()
    text = models.TextField(_('Усыныс'), blank=False)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Запросы пользователей'
        verbose_name_plural = 'Запросы пользователей'
