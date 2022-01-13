from django.conf import settings
from django.core import serializers
from django.http import HttpResponse
from django.views import View

from .helper import get_current_rate
from .models import ExchangeRate


class QuotesEndpoint(View):

    serialized_fields = ('exchange_rate', 'last_refreshed')

    def get(self, request):
        exchange_rate = ExchangeRate.objects.all().order_by('last_refreshed')
        er_list = serializers.serialize('json', exchange_rate, fields=self.serialized_fields)
        return HttpResponse(er_list, content_type="text/json-comment-filtered")

    def post(self, request):
        er = get_current_rate(settings.BTC_TICKER, settings.USD_TICKER)

        serialized_obj = serializers.serialize('json', [er], fields=self.serialized_fields)
        return HttpResponse(serialized_obj, content_type="text/json-comment-filtered")
