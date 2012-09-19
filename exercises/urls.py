from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('exercises.views',
    url(r'^home/', 'index', name='home'),

)
