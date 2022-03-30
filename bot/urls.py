from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from oraza_bot.settings import TELEGRAM_TOKEN
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path(f'{TELEGRAM_TOKEN}/',
         csrf_exempt(views.TelegramBotWebhookView.as_view())),

]
