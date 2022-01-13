from alpha_vantage.cryptocurrencies import CryptoCurrencies
from dateutil import parser
from django.conf import settings


def get_current_rate(from_ticker, to_ticker):
    av_api_key = settings.ALPHAVANTAGE_API_KEY
    cc = CryptoCurrencies(key=av_api_key)
    resp, _ = cc.get_digital_currency_exchange_rate(from_ticker, to_ticker)

    from myapp.models import ExchangeRate
    return ExchangeRate.objects.create(
        from_currency_code=resp['1. From_Currency Code'],
        to_currency_code=resp['3. To_Currency Code'],
        exchange_rate=resp['5. Exchange Rate'],
        last_refreshed=parser.parse(resp['6. Last Refreshed']),
    )
