from operator import mod
from django.db import models
from django.utils.translation import gettext_lazy as _

ACTIONS = (
    (0, 'Ораза кестесі'),
    (1, 'Қадір түні'),
    (2, 'Дұғалар'),
    (3, 'Сұрақ жауап (FAQ)'),
    (4, 'Ұсыныс, сын'),
    (5, 'Чатқа қосылу'),
    (6, 'Рамазан жоспары'),
    (7, 'Оқылу керек дұғалар'),
    (8, 'Сұрақ-жауап (қадір туні)'),
    (9, 'Қадір түні жайында'),
    (10, 'Қадір түнінде 10 сауапты іс'),
    (11, 'Қадір түнінде 10 күнәлі іс'),
    (12, 'Істелуі тиіс ең таңдаулы амалдар'),
    (13, 'Артқа'),
    (14, 'Хадистер'),
    (15, 'Рамазан күнделік')
)


class Action(models.Model):
    command = models.IntegerField(_('Комманда'), blank=True, choices=ACTIONS)
    name_kk = models.CharField(
        _('Название комманды (каз)'), max_length=100, blank=True)
    name_ru = models.CharField(
        _('Название комманды (рус)'), max_length=100, blank=True)
    link = models.CharField(
        _('Ссылка (если комманда link)'), max_length=5000, blank=True)

    def __str__(self):
        return self.name_ru

    class Meta:
        verbose_name = 'Действия'
        verbose_name_plural = 'Действия'
