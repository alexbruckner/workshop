from django.db import models
from django.contrib.auth.models import User
from django import forms

class UserProfile(models.Model):
	
	user = models.OneToOneField(User)		

	def __unicode__(self):
        	return self.user	
	

class Lecturer(User):
	pass        

class Student(User):
        pass

class Exercise(models.Model):
        title = models.CharField(max_length=100)
        description = models.TextField()
        question = models.TextField()
        created = models.DateTimeField(auto_now_add=True)

        def __unicode__(self):
                return self.title

class Lecture(models.Model):
        title = models.CharField(max_length=100)
        description = models.TextField()
        content = models.TextField()
        exercises = models.ManyToManyField(Exercise, through='Practice')
	created = models.DateTimeField(auto_now_add=True)

        def __unicode__(self):
                return self.title


class Course(models.Model):
	title = models.CharField(max_length=100)	
	description = models.TextField()
	lecturer = models.ForeignKey(Lecturer, null=True, blank=True)
	students = models.ManyToManyField(Student, through='Subscription')
	lectures = models.ManyToManyField(Lecture, through='Curriculum')
	created = models.DateTimeField(auto_now_add=True)

        def __unicode__(self):
		return '%s (lecturer: %s)' % (self.title, str(self.lecturer))


class Practice(models.Model):
	lecture = models.ForeignKey(Lecture)
	exercise = models.ForeignKey(Exercise)
	created = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
                return '%s (exercise: %s)' % (str(self.lecture), str(self.exercise))


class Curriculum(models.Model):
	course = models.ForeignKey(Course)
	lecture = models.ForeignKey(Lecture)
	created = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
                return '%s (lecture: %s)' % (str(self.course), str(self.lecture))	

class Submission(models.Model):
	exercise = models.ForeignKey(Exercise)
	student = models.ForeignKey(Student)
	answer = models.TextField()
	created = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return '%s (student: %s)' % (str(self.exercise), str(self.student))


class Mark(models.Model):
        submission = models.ForeignKey(Submission)
        lecturer = models.ForeignKey(Lecturer)
        mark = models.IntegerField()
        created = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return '%s (marked by: %s)' % (str(self.submission), str(self.lecturer))


class Subscription(models.Model):
	course = models.ForeignKey(Course)
	student = models.ForeignKey(Student)
	created = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return '%s (student: %s)' % (str(self.course), str(self.student))




