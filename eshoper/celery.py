from __future__ import absolute_import, unicode_literals

import logging
import os

from celery import Celery
from celery.schedules import crontab, timedelta
from django.conf import settings

logger = logging.getLogger("Celery")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eshoper.settings')
app = Celery('eshoper')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.beat_schedule = {
    'send-mail-task': {
        'task': 'core.tasks.send_mail_task',
        'schedule': crontab(hour=15, minute=0, day_of_week=5),  # every 30 seconds
    },
}
# app.conf.beat_schedule = {
#     'send_sms_to_customs_task': {
#         'task': 'import_orders.tasks.send_sms_to_customs_task',
#         'schedule': crontab(hour=10, minute=0),
#     },
#     'send_sms_after_arrival_at_factory_task': {
#         'task': 'export_orders.tasks.send_sms_after_arrival_at_factory_task',
#         'schedule': crontab(minute=0),
#     },
#     'send_sms_to_logistics_to_remind_swb_draft': {
#         'task': 'export_orders.tasks.send_sms_to_logistics_to_remind_swb_draft',
#         'schedule': crontab(hour=10, minute=0),
#     },
#     'send_sms_to_logistics_to_remind_swb_final': {
#         'task': 'export_orders.tasks.send_sms_to_logistics_to_remind_swb_final',
#         'schedule': crontab(hour=10, minute=0),
#     },
# }
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

if not settings.DEBUG:
    app.conf.update(
        BROKER_URL='redis://:{password}@redis:6379/0'.format
        (password='dKqs72RhtaPPYyfN'),
        CELERYBEAT_SCHEDULER='django_celery_beat.schedulers:DatabaseScheduler',
        CELERY_RESULT_BACKEND='redis://:{password}@redis:6379/1'.format(
            password='dKqs72RhtaPPYyfN'
        ),
        CELERY_DISABLE_RATE_LIMITS=True,
        CELERY_ACCEPT_CONTENT=['json', ],
        CELERY_TASK_SERIALIZER='json',
        CELERY_RESULT_SERIALIZER='json',
        CELERY_TIMEZONE='America/New_York',
    )
else:
    app.conf.update(
        BROKER_URL='redis://localhost:6379/0',
        CELERYBEAT_SCHEDULER='django_celery_beat.schedulers:DatabaseScheduler',
        CELERY_RESULT_BACKEND='redis://localhost:6379/1',
        CELERY_DISABLE_RATE_LIMITS=True,
        CELERY_ACCEPT_CONTENT=['json', ],
        CELERY_TASK_SERIALIZER='json',
        CELERY_RESULT_SERIALIZER='json',
        CELERY_TIMEZONE='America/New_York',
    )