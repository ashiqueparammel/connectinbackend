from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'connectin.settings')
app = Celery('connectin')
app.conf.enable_utc = False
app.conf.update( timezone=settings.CELERY_TIMEZONE,enable_utc=False,)
app.config_from_object(settings, namespace='CELERY')
app.autodiscover_tasks()

print(app.conf.broker_url)
print(app.conf.result_backend)
@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
    print('working...................................')


