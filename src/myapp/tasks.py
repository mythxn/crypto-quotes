from __future__ import absolute_import
from __future__ import unicode_literals

import logging

from core.celery import app
from django.conf import settings

from .helper import get_latest_er

logger = logging.getLogger("celery")


@app.task
def hourly_get_quotes():
    get_latest_er(settings.BTC_TICKER, settings.USD_TICKER)

