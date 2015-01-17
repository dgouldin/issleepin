from __future__ import absolute_import
from django.conf.urls import patterns, include, url
from django.contrib import admin

import main.views

urlpatterns = patterns('',
    url(r'^$', main.views.profile),
    url(r'^claim/$', main.views.claim),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
