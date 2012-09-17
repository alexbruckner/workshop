from exercises.models import Lecturer, Student, Mark, Submission, Exercise, Course, Subscription
from django.contrib import admin

admin.site.register(Lecturer)
admin.site.register(Student)
admin.site.register(Mark)
admin.site.register(Submission)

class ExerciseAdmin(admin.ModelAdmin):
	list_display = ('title', 'course')
        list_filter = ('title', 'course')
        ordering = ('-created',)
        search_fields = ('title',)


admin.site.register(Exercise, ExerciseAdmin)

class CourseAdmin(admin.ModelAdmin):
	list_display = ('title', 'lecturer', 'created')
        list_filter = ('title', 'lecturer')
        ordering = ('-created',)
        search_fields = ('title',)

admin.site.register(Course, CourseAdmin)
admin.site.register(Subscription)

