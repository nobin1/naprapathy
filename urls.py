from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template 
import os
static = os.path.join(os.path.dirname(__file__), 'static')

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/(.*)', admin.site.root), 
    (r'^$', direct_to_template, {'template': 'index.html'}),
    (r'^contact/', direct_to_template, {'template': 'maps.html'}),
    (r'^services/', direct_to_template, {'template': 'services.html'}),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
		{'document_root': static}),
	#(r'^i18n/', include('django.conf.urls.i18n')),
)
