from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ev_charging.settings')
app = Celery('ev_charging')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()