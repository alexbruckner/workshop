from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import redirect_to

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

	url(r'^$', redirect_to, {'url': '/exercises/'}),

	# Login / logout.
    	url(r'^login/$', 'django.contrib.auth.views.login'),
	url(r'^logout/$', 'django.contrib.auth.views.logout'),
	
	url(r'^exercises/', include('exercises.urls')),

	# Uncomment the next line to enable the admin:
    	url(r'^admin/', include(admin.site.urls)),
)
