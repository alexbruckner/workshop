from django.db import models

class User(models.Model):
	username = models.CharField(max_length=20)
	email = models.CharField(max_length=50)
	firstname = models.CharField(max_length=20)
	lastname = models.CharField(max_length=20)
	created = models.DateTimeField(auto_now_add=True)
	active = models.BooleanField()

	def __unicode__(self):
        	return self.username	
	

class Lecturer(User):
	pass        

class Student(User):
        pass

class Course(models.Model):
	title = models.CharField(max_length=100)	
	description = models.TextField()
	lecturer = models.ForeignKey(Lecturer,blank=True)
	students = models.ManyToManyField(Student, through='Subscription')
	created = models.DateTimeField(auto_now_add=True)

        def __unicode__(self):
		return '%s (lecturer: %s)' % (self.title, str(self.lecturer))

class Exercise(models.Model):
	course = models.ForeignKey(Course)
	title = models.CharField(max_length=100)
	description = models.TextField()
	question = models.TextField()
    	created = models.DateTimeField(auto_now_add=True)
	
	def __unicode__(self):
		return '%s (course: %s)' % (self.title, str(self.course))

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

