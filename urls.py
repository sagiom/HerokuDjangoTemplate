#encoding: utf-8
# just for testing git function
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'digilink.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url("^$", "views.index", name="index"),
    
    url(r'^admin/', include(admin.site.urls)),

)

if not settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_URL}),
    )
