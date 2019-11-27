from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

##Defines the model to store all the post-related details
class Posts(models.Model):

	##The title of the post
	job_title = models.CharField(max_length=200)
	##Location of the job	
	job_location = models.CharField(max_length=100,default="HostelXYZ")
	##date of job	
	job_date = models.DateTimeField("job date",default=datetime.now())
	##A brief description of the job	
	job_details = models.TextField()
	##Date when the post was published
	post_published = models.DateTimeField("date published",default=datetime.now())
	##username of the person who created the post	
	author = models.CharField(max_length=200,default="Author")
	def __str__(self):
		return self.job_title

##Defines the model to store all the leave_requests-related details
class Leave(models.Model):
	##Start date of the leave period
	start_date = models.DateField("start date")
	##Total no of days in the leave period	
	no_of_days = models.IntegerField()
	##Reason for the leave request	
	reason = models.TextField()
	##Approval status of the request
	approved = models.BooleanField(default='false')
	##username of the staff who applied for the leave	
	author = models.CharField(max_length=200,default="Author")
	def __str__(self):
		return self.reason

##Defines the model to store all the staff-supervisor mappings
class dependent(models.Model):
	
	##Username of the staff
	staff_name = models.CharField(max_length=200, default="DUMMY")
	##Username of the supervisor	
	supervisor_name = models.CharField(max_length=200)
	def __str__(self):
		return self.staff_name

