from django.conf.urls.defaults import patterns, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('storage.views',
    url(r'^$', 'index'),
    url(r'^items/', 'items'),
)
