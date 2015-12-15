from django.conf.urls import include, url, patterns
from django.contrib import admin

from scanner.site.views import Home

urlpatterns = patterns(
    '',
    url(r'^$', Home.as_view(), name='site.home'),
)
