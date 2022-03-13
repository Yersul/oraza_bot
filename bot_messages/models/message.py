from operator import mod
from statistics import mode
from django.db import models
from django.utils.translation import gettext_lazy as _
from bot.models import User

from bot_messages.models.action import Action


MESSAGE_TYPE = (
    (0, _('Не выбрано')),
    (1, _('Стартовое сообщение')),
    (2, _('Меню')),
    (3, _('Выбор города')),
    (4, _('Қадір түні')),
    (5, _('Дұғалар')),
    (6, _('Рамазан жоспары')),
    (7, _('Рамазан жайлы сұрақтар')),
    (8, _('Ұсыныс')),
)

INLINE_BTN_COUNT = (
    (1, '1 кнопка'),
    (2, '2 кнопки'),
    (3, '3 кнопки'),
    (4, '4 кнопки'),
)


class Message(models.Model):
    message_kk = models.TextField(
        _('Сообщение (каз)'), max_length=1000, blank=True)
    message_ru = models.TextField(
        _('Сообщение (рус)'), max_length=1000, blank=True)

    type = models.PositiveIntegerField(
        _('Тип сообщения'), default=0, choices=MESSAGE_TYPE)
    inline_count = models.PositiveIntegerField(
        _('Количество кнопок в одной линии'), default=1, choices=INLINE_BTN_COUNT)
    actions = models.ManyToManyField(Action, blank=True)

    def __str__(self):
        return str(MESSAGE_TYPE[self.type][1])

    @classmethod
    def get_text_obj(cls, type=0):
        return cls.objects.filter(type=type).last()

    @classmethod
    def get_text(cls, user: User = None, type=0) -> str:
        if(not user == None):
            return Message.get_text_with_user(user, type)
        else:
            return cls.objects.filter(type=type).last().message_kk

    @classmethod
    def get_text_with_user(cls, user: User, type=0) -> str:
        user_name = user.first_name
        try:
            text = cls.objects.filter(type=type).last().message_kk
        except:
            text = 'Ошибка)'
        return text.format(name=user_name)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщение'
