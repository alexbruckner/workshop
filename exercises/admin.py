from exercises.models import Lecturer, Student, Mark, Submission, Exercise, Course, Subscription
from django.contrib import admin

class UserAdmin(admin.ModelAdmin):
	list_display = ('username', 'firstname', 'lastname', 'email', 'created')
        list_filter = ('username', 'firstname', 'lastname', 'created')
        ordering = ('username',)
        search_fields = ('username','firstname','lastname')

admin.site.register(Lecturer, UserAdmin)
admin.site.register(Student, UserAdmin)

class MarkAdmin(admin.ModelAdmin):
	list_display = ('submission', 'lecturer', 'mark', 'created')
        list_filter = ('submission__exercise__title', 'lecturer__username', 'mark', 'created')
        ordering = ('-created',)
        search_fields = ('lecturer__username', 'mark')

admin.site.register(Mark, MarkAdmin)

class SubmissionAdmin(admin.ModelAdmin):
	list_display = ('exercise', 'student', 'created')
        list_filter = ('exercise__title', 'student__username', 'created')
        ordering = ('-created',)

admin.site.register(Submission, SubmissionAdmin)

class ExerciseAdmin(admin.ModelAdmin):
	list_display = ('title', 'course')
        list_filter = ('title', 'course__title')
        ordering = ('-created',)
        search_fields = ('title',)

admin.site.register(Exercise, ExerciseAdmin)

class CourseAdmin(admin.ModelAdmin):
	list_display = ('title', 'lecturer', 'created')
        list_filter = ('title', 'lecturer__username' ,'created')
        ordering = ('-created',)
        search_fields = ('title',)

admin.site.register(Course, CourseAdmin)

class SubscriptionAdmin(admin.ModelAdmin):
	list_display = ('course', 'student', 'created')
        list_filter = ('course__title', 'student__username' ,'created')
        ordering = ('-created',)
        search_fields = ('course__title','student__username')

admin.site.register(Subscription, SubscriptionAdmin)

