import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oraza_bot.settings')
app = Celery('oraza_bot')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.conf.enable_utc = False

    