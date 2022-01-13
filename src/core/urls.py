from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from myapp.views import QuotesEndpoint

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/quotes/', QuotesEndpoint.as_view()),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
