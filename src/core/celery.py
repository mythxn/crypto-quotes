from __future__ import absolute_import
from __future__ import unicode_literals

import logging
import os

from celery import Celery

logger = logging.getLogger("Celery")

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'pull-current-rate': {
        'task': 'myapp.tasks.hourly_get_quotes',
        'schedule': 3600,
    },
}

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
