import os
from celery import Celery
from Board.Board import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings)

app = Celery('Board')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(settings.INSTALLED_APPS, related_name='tasks')




