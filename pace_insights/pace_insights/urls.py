from django.conf.urls import patterns, include, url
from django.contrib import admin
from depreciation import urls as depreciation_urls


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^depreciation/', include(depreciation_urls)),
)
