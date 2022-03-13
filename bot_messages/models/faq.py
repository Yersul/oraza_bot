from unicodedata import category
from django.db import models
from django.utils.translation import gettext_lazy as _


class FAQCategory(models.Model):
    category_kk = models.CharField(
        _('Название категории (каз)'), max_length=255)
    category_ru = models.CharField(
        _('Название категории (рус)'), max_length=255)

    def __str__(self):
        return self.category_kk

    class Meta:
        verbose_name = 'Категория вопроса'
        verbose_name_plural = 'Категория вопросов'



class FAQ(models.Model):
    question_kk = models.CharField(_('Вопрос (каз)'), max_length=255)
    question_ru = models.CharField(_('Вопрос (рус)'), max_length=255)
    body_kk = models.TextField(
        _('Ответ (каз)'), max_length=4096, blank=True)
    body_ru = models.TextField(
        _('Ответ (рус)'), max_length=4096, blank=True)
    link = models.CharField(
        _('Ссылка на источник'), max_length=4096, blank=True)
    category = models.ForeignKey(
        FAQCategory, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.question_kk

    class Meta:
        verbose_name = 'Вопрос-ответ'
        verbose_name_plural = 'Вопрос-ответ'
