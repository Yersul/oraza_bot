from django.core.management.base import BaseCommand, CommandError
from bot.dispatcher import run_pooling
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oraza_bot.settings')
django.setup()


class Command(BaseCommand):
    help = "Запускает бота"

    def handle(self, *args, **options):
        run_pooling()
