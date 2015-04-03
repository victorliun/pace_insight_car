from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from depreciation import urls as depreciation_urls
from depreciation.views import home, about

urlpatterns = patterns('',
    url(r'^$', home),
    url(r'^about/$', about),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^depreciation/', include(depreciation_urls)),
)

urlpatterns += patterns('',
    # ... the rest of your URLconf goes here ...
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
