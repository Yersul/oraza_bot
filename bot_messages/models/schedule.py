from tabnanny import verbose
from django.db import models
from django.utils.translation import gettext_lazy as _
from bot_messages.models.city import City


class Schedule(models.Model):
    image = models.ImageField(_('Фото расписания'),
                              blank=True, upload_to='schedules')
    text = models.TextField(_('Текст'), max_length=500, blank=True)
    link = models.CharField(
        _('Ссылка на источник'), max_length=1000, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.city.name_ru

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписание'
