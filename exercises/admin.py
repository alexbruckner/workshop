from exercises.models import Lecturer, Student, Mark, Submission, Exercise, Course, Subscription
from django.contrib import admin

admin.site.register(Lecturer)
admin.site.register(Student)
admin.site.register(Mark)
admin.site.register(Submission)
admin.site.register(Exercise)

class CourseAdmin(admin.ModelAdmin):
	list_display = ('title', 'lecturer', 'created')
        list_filter = ('title', 'lecturer')
        ordering = ('-created',)
        search_fields = ('title',)

admin.site.register(Course, CourseAdmin)
admin.site.register(Subscription)

