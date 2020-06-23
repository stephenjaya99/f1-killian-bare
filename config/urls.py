from django.conf import settings
from django.contrib import admin
from django.urls import include
from django.urls import re_path

from killian.api import urls as api_urls
from killian.views import main

admin.autodiscover()

urlpatterns = [
    re_path(r'^$', main.index, name='index'),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^admin/django-rq/', include('django_rq.urls')),
    re_path(r'^api/v1/', include(api_urls))
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        re_path(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
