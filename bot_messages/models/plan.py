from django.db import models
from django.utils.translation import gettext_lazy as _


class Plan(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(_('Фото рамазана'),
                              blank=True, upload_to='ramazan')
    text = models.TextField(_('Текст'), max_length=500, blank=True)
    link = models.CharField(
        _('Ссылка на источник'), max_length=1000, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'План'
        verbose_name_plural = 'План'
