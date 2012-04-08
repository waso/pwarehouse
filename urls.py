from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import redirect_to
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'storage.views.index'),
    url(r'^items/', 'storage.views.items'),
    url(r'^categories/', 'storage.views.categories'),
    url(r'^storages/', 'storage.views.storages'),
    url(r'^clients/add/', 'storage.views.clients_add'),
    url(r'^clients/', 'storage.views.clients'),
    url(r'^documents/invoice/add', 'storage.views.invoice_add'),
    url(r'^documents/invoice', 'storage.views.invoice'),
    url(r'^documents/mmplus', 'storage.views.mmplus'),
    url(r'^documents/mmminus', 'storage.views.mmminus'),
    url(r'^documents/pz', 'storage.views.pz'),
    url(r'^documents/wz', 'storage.views.wz'),
    url(r'^documents/', 'storage.views.documents'),
    url(r'^reports/', 'storage.views.reports'),
)
