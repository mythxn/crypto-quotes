from django.http import HttpResponse
from django.views import View

from .tasks import show_hello_world


class QuotesEndpoint(View):
    def get(self, request):
        return HttpResponse('result')

    def post(self, request):
        show_hello_world.apply()
        return HttpResponse('result from post')