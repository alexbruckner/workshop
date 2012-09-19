# Create your views here.
from django.shortcuts import render_to_response
from exercises.models import Course
def index(request):
	return render_to_response('exercises/index.html', {'course_list': Course.objects.all().order_by('-created')})
