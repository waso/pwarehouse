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
    url(r'^documents/invoice/(\d+)$', 'storage.invoice_views.invoice_view'),
    url(r'^documents/invoice/add', 'storage.invoice_views.invoice_add'),
    url(r'^documents/invoice', 'storage.invoice_views.invoice'),
    url(r'^documents/mm/(\d+)$', 'storage.mm_views.view'),
    url(r'^documents/mm/add', 'storage.mm_views.add'),
    url(r'^documents/mm', 'storage.mm_views.mm'),
    url(r'^documents/pz', 'storage.views.pz'),
    url(r'^documents/wz', 'storage.views.wz'),
    url(r'^documents/', 'storage.views.documents'),
    url(r'^reports/', 'storage.views.reports'),
)
