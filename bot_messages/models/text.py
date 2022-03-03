from django.db import models
from django.utils.translation import gettext_lazy as _

from bot_messages.models.pray import Pray


class Text(models.Model):
    text_kk = models.TextField(_('текст (каз)'), max_length=4096, blank=False, null=True)
    text_ru = models.TextField(_('текст (рус)'), max_length=4096, blank=False, null=True) 
    pray = models.ForeignKey(Pray, models.CASCADE, related_name='text', null = True)
