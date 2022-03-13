from operator import mod
from statistics import mode
from django.db import models
from django.utils.translation import gettext_lazy as _
from bot.models import User


class AbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Request(AbstractModel):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    text = models.TextField(_('Усыныс'), blank=False)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Запрос пользователя'
        verbose_name_plural = 'Запросы пользователей'
