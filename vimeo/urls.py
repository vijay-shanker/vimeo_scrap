from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from apps.items.views import search_core

from apps.items.views import Home
urlpatterns = patterns('',
    # Examples:
    url(r'^$', Home.as_view(), name='home'),
    url(r'^search/', 'apps.items.views.search_core', name="search_core"),
    # url(r'^vimeo/', include('vimeo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
