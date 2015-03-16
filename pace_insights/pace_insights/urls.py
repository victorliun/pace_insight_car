from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from depreciation import urls as depreciation_urls
from depreciation.views import home

urlpatterns = patterns('',
    url(r'^$', home),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^depreciation/', include(depreciation_urls)),
)

urlpatterns += patterns('',
    (r'^static/(.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),)