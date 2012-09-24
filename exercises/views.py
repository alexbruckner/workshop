from django.shortcuts import render_to_response
from exercises.models import Course
from django.template import RequestContext
def index(request):
    return render_to_response('exercises/index.html', {'course_list': Course.objects.all()},RequestContext(request))
