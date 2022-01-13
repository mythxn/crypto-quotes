from django.db import models


class ExchangeRate(models.Model):
    id = models.AutoField(primary_key=True)
    from_currency_code = models.CharField(max_length=200)
    to_currency_code = models.CharField(max_length=200)
    exchange_rate = models.FloatField()
    last_refreshed = models.DateTimeField()
