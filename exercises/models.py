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
        
	def __unicode__(self):
                return '%s (Lecturer)' % self.username
	

class Student(User):
        
	def __unicode__(self):
                return '%s (Student)' % self.username


class Submission(models.Model):
	student = models.ForeignKey(Student)
	answer = models.TextField()
	created = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
	        return self.student


class Mark(models.Model):
        submission = models.ForeignKey(Submission)
        lecturer = models.ForeignKey(Lecturer)
        mark = models.IntegerField()
        created = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
	        return self.submission


class Exercise(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	question = models.TextField()
    	pub_date = models.DateTimeField(auto_now_add=True)
	submissions = models.ManyToManyField(Submission, blank=True)

	def __unicode__(self):
                return self.title


class Course(models.Model):
	title = models.CharField(max_length=100)	
	description = models.TextField()
	lecturer = models.ManyToManyField(Lecturer,blank=True)
	students = models.ManyToManyField(Student, blank=True)
	excercises = models.ManyToManyField(Exercise, blank=True)	

        def __unicode__(self):
                return self.title


