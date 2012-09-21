from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import redirect_to

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

	url(r'^$', redirect_to, {'url': '/exercises/course'}),
	
	url(r'^exercises/', include('exercises.urls')),

	# Uncomment the next line to enable the admin:
    	url(r'^admin/', include(admin.site.urls)),
)
