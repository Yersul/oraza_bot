from unicodedata import category
from django.db import models
from django.utils.translation import gettext_lazy as _

FAQ_CATEGORY = (
    (0, 'обычный'),
    (1, 'Молитва'),
    (2, 'Кадір түні'),
)


class FAQ(models.Model):
    question_kk = models.CharField(_('Вопрос (каз)'), max_length=255)
    question_ru = models.CharField(_('Вопрос (рус)'), max_length=255)
    body_kk = models.TextField(
        _('Ответ (каз)'), max_length=1000, blank=True)
    body_ru = models.TextField(
        _('Ответ (рус)'), max_length=1000, blank=True)
    link = models.CharField(
        _('Ссылка на источник'), max_length=1000, blank=True)

    category = models.IntegerField(
        _('Тип ответа'), default=0, choices=FAQ_CATEGORY)

    def __str__(self):
        return self.question_kk

    class Meta:
        verbose_name = 'Вопрос-ответ'
        verbose_name_plural = 'Вопрос-ответ'
