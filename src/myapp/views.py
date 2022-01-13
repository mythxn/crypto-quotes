from django.conf import settings
from django.core import serializers
from django.http import HttpResponse
from django.views import View

from .helper import get_latest_er
from .models import ExchangeRate


class QuotesEndpoint(View):

    def get(self, request):
        exchange_rate = ExchangeRate.objects.all().order_by('last_refreshed')
        er_list = serializers.serialize('json', exchange_rate, fields=('exchange_rate', 'last_refreshed'))
        return HttpResponse(er_list, content_type="text/json-comment-filtered")

    def post(self, request):
        er = get_latest_er(settings.BTC_TICKER, settings.USD_TICKER)

        serialized_obj = serializers.serialize('json', [er], fields=('exchange_rate', 'last_refreshed'))
        return HttpResponse(serialized_obj, content_type="text/json-comment-filtered")
