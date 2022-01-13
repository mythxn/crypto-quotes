from alpha_vantage.cryptocurrencies import CryptoCurrencies
from dateutil import parser
from django.conf import settings
from django.core import serializers
from django.http import HttpResponse
from django.views import View

from .models import ExchangeRate


class QuotesEndpoint(View):
    BTC_TICKER = 'BTC'
    USD_TICKER = 'USD'

    def get(self, request):
        exchange_rate = ExchangeRate.objects.all().order_by('last_refreshed')
        er_list = serializers.serialize('json', exchange_rate, fields=('exchange_rate', 'last_refreshed'))
        return HttpResponse(er_list, content_type="text/json-comment-filtered")

    def post(self, request):
        av_api_key = settings.ALPHAVANTAGE_API_KEY
        cc = CryptoCurrencies(key=av_api_key)
        resp, _ = cc.get_digital_currency_exchange_rate(self.BTC_TICKER, self.USD_TICKER)

        er = ExchangeRate.objects.create(
            from_currency_code=resp['1. From_Currency Code'],
            to_currency_code=resp['3. To_Currency Code'],
            exchange_rate=resp['5. Exchange Rate'],
            last_refreshed=parser.parse(resp['6. Last Refreshed']),
        )

        serialized_obj = serializers.serialize('json', [er], fields=('exchange_rate', 'last_refreshed'))
        return HttpResponse(serialized_obj, content_type="text/json-comment-filtered")
