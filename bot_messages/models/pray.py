from tabnanny import verbose
from django.db import models
from django.utils.translation import gettext_lazy as _
from bot_messages.models.city import City


PRAY_TYPE = (
    (0, 'Дұға'),
    (1, 'Кадір түні'),
)


class Pray(models.Model):
    name_kk = models.CharField(_('Название (каз)'), max_length=255)
    name_ru = models.CharField(_('Название (рус)'), max_length=255)
    link = models.CharField(
        _('Ссылка на источник'), max_length=1000, blank=True)
    pray_type = models.IntegerField(_('Тип'), default=0, choices=PRAY_TYPE)

    def __str__(self):
        return self.name_kk

    class Meta:
        verbose_name = 'Молитва'
        verbose_name_plural = 'Молитвы'
