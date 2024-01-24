from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab
from datetime import datetime, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'connectin.settings')
app = Celery('connectin')
app.conf.enable_utc = False
app.conf.update( timezone=settings.CELERY_TIMEZONE,enable_utc=False,)
app.config_from_object(settings, namespace='CELERY')



# def get_schedule_for_next_minute():
#     current_time = datetime.now()
#     next_minute_time = current_time + timedelta(minutes=1)

#     # Convert the time to crontab schedule format
#     crontab_schedule = crontab(
#         minute=next_minute_time.minute,
#         hour=next_minute_time.hour,
#         day_of_week=next_minute_time.strftime('%a'),  # Day of the week (e.g., 'Mon', 'Tue')
#         day_of_month=next_minute_time.day,
#         month_of_year=next_minute_time.month,
#     )

#     return crontab_schedule

# app.conf.beat_schedule = {

#     'send-mail-block':{
#         'task':'employee.tasks.JobBlockSendingMail',
#         'schedule':get_schedule_for_next_minute(),
#         'options':{"expires":60}
#     },
        

# }

app.autodiscover_tasks()





print(app.conf.broker_url)
print(app.conf.result_backend)
@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
    print('working...................................')


