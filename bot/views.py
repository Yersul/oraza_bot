import json
import logging
from django.views import View
from django.http import JsonResponse

from oraza_bot.settings import DEBUG
from bot.dispatcher import process_telegram_event

logger = logging.getLogger(__name__)


def index(request):
    return JsonResponse({"error": "sup hacker"})


class TelegramBotWebhookView(View):
    def post(self, request, *args, **kwargs):
        logger.info(f"Get webhook post")
        process_telegram_event(json.loads(request.body))
        return JsonResponse({"ok": "POST request processed"})

    def get(self, request, *args, **kwargs):
        logger.info(f"Get webhook get")
        return JsonResponse({"ok": "Get request received! But nothing done"})
