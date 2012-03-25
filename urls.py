from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import redirect_to
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MotoHurt.views.home', name='home'),
    # url(r'^MotoHurt/', include('MotoHurt.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'storage.views.index'),
    url(r'^items/', 'storage.views.items'),
    url(r'^documents/', 'storage.views.documents'),
    url(r'^reports/', 'storage.views.reports'),
)
