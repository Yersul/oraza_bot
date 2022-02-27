from django.contrib import admin
from bot_messages.models.city import City
from bot_messages.models.faq import FAQ
from bot_messages.models.message import Message
from bot_messages.models.action import Action
from bot_messages.models.pray import Pray
from bot_messages.models.request import Request
from bot_messages.models.schedule import Schedule


admin.site.register(Message)
admin.site.register(City)
admin.site.register(Action)
admin.site.register(FAQ)
admin.site.register(Request)
admin.site.register(Schedule)
admin.site.register(Pray)
