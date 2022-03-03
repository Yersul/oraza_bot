from django.contrib import admin
from bot_messages.models.city import City
from bot_messages.models.faq import FAQ
from bot_messages.models.message import Message
from bot_messages.models.action import Action
from bot_messages.models.pray import Pray
from bot_messages.models.request import Request
from bot_messages.models.schedule import Schedule
from bot_messages.models.text import Text


class TextAdmin(admin.TabularInline):
    model = Text
    extra = 0

class PrayAdmin(admin.ModelAdmin):
    inlines = [TextAdmin, ]

class ScheduleAdmin(admin.TabularInline):
    model = Schedule
    extra = 0
    max_num = 1

class CityAdmin(admin.ModelAdmin):
  inlines=[ScheduleAdmin]


admin.site.register(Message)
admin.site.register(City, CityAdmin)
admin.site.register(Action)
admin.site.register(FAQ)
admin.site.register(Request)
admin.site.register(Pray, PrayAdmin)
