from operator import mod
from django.db import models
from django.utils.translation import gettext_lazy as _


CITY_TYPE = (
    (0, 'Регион'),
    (1, 'Город')
)


class City(models.Model):
    name_kk = models.CharField(_('Название (каз)'), max_length=100, blank=True)
    name_ru = models.CharField(_('Название (рус)'), max_length=100, blank=True)

    type = models.IntegerField(default=0, choices=CITY_TYPE)

    def __str__(self):
        return self.name_ru

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

