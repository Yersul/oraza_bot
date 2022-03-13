from django.db import models
from django.utils.translation import gettext_lazy as _
import random


class Chadis(models.Model):
    text_kk = models.TextField(
        _('хадис (каз)'), max_length=4096, blank=False, null=True)
    text_ru = models.TextField(
        _('хадис (рус)'), max_length=4096, blank=False, null=True)

    @classmethod
    def rand_obj(cls):
        n = random.randint(0, cls.objects.count()-1)
        list = cls.objects.all()
        return list[n]
