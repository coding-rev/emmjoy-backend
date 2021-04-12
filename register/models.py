from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class EmmjoyUsers(AbstractUser):
	email 			= models.EmailField(unique=True)
	phone 			= models.CharField(max_length=20, blank=True, null=True, unique=True)
	is_tutor 		= models.BooleanField(default=False)
	is_student 		= models.BooleanField(default=True)

	def __str__(self):
		return self.username

	class Meta:
		verbose_name_plural = "Emmjoy Users"