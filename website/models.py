from django.db import models
from register.models import EmmjoyUsers
# Create your models here.

class Courses(models.Model):
	tutor 			= models.ForeignKey(EmmjoyUsers, on_delete=models.CASCADE)
	image 			= models.ImageField(blank=True, null=True)
	title 			= models.CharField(max_length=100)
	price 			= models.CharField(max_length=100)
	duration 		= models.CharField(max_length=100)
	date_posted 	= models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name_plural = "Courses"
