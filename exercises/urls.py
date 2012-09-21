from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from exercises.models import Course

urlpatterns = patterns('',

	url(r'^course/$',
		ListView.as_view(
            	queryset=Course.objects.order_by('-created'),
            	context_object_name='course_list',
            	template_name='exercises/index.html'),
        	name='course_index'),

	url(r'^course/(?P<pk>\d+)/$',
        	DetailView.as_view(
            	model=Course,
            	template_name='exercises/course.html'),
        	name='course_detail'),
    	

)
