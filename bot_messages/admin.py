from django.contrib import admin
from bot_messages.models.chadis import Chadis
from bot_messages.models.city import City
from bot_messages.models.faq import FAQ, FAQCategory
from bot_messages.models.message import Message
from bot_messages.models.action import Action
from bot_messages.models.plan import Plan
from bot_messages.models.pray import Pray
from bot_messages.models.request import Request
from bot_messages.models.schedule import Schedule
from bot_messages.models.text import Text


class TextAdmin(admin.TabularInline):
    model = Text
    extra = 0


class PrayAdmin(admin.ModelAdmin):
    list_display = ('name_kk', 'action', )
    list_filter = ('pray_type',)
    inlines = [TextAdmin, ]


class ScheduleAdmin(admin.TabularInline):
    model = Schedule
    extra = 0
    max_num = 1


class CityAdmin(admin.ModelAdmin):
    list_filter = ('type', )
    inlines = [ScheduleAdmin]


class FAQAdmin(admin.TabularInline):
    model = FAQ
    extra = 0


class FAQCategortyAdmin(admin.ModelAdmin):
    inlines = [FAQAdmin, ]


admin.site.register(Message)
admin.site.register(City, CityAdmin)
admin.site.register(Action)
admin.site.register(FAQ)
admin.site.register(FAQCategory, FAQCategortyAdmin)
admin.site.register(Request)
admin.site.register(Pray, PrayAdmin)
admin.site.register(Plan)
admin.site.register(Chadis)
