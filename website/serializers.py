from rest_framework import serializers
from register.models import EmmjoyUsers
from .models import *

class RegistrationSerializer(serializers.ModelSerializer):
	class Meta:
		model  		= EmmjoyUsers
		fields  	= ['username', 'email', 'phone', 'password']


class CoursesSerializer(serializers.ModelSerializer):
	class Meta:
		model 		= Courses
		fields 		= '__all__'

# class CoursesSerializer(serializers.Serializer):
# 	tutor 			= serializers.ForeignKey(EmmjoyUsers, on_delete=models.CASCADE)
# 	title 			= serializers.CharField(max_length=100)
# 	image 			= serializers.ImageField()
# 	price 			= serializers.CharField(max_length=100)
# 	duration 		= serializers.CharField(max_length=100)
# 	date_posted 	= serializers.DateTimeField(auto_now_add=True)

# 	def create(self, validated_data):
#  		return Courses.objects.create(validated_data)

#  	def update(self, instance, validated_data):
#  		instance.tutor			= validated_data.get('tutor', instance.tutor)
#  		instance.title 			= validated_data.get('title', instance.title)
#  		instance.image 			= validated_data.get('image', instance.image)
#  		instance.price 			= validated_data.get('price', instance.price)
#  		instance.duration 		= validated_data.get('duration', instance.duration)
#  		instance.date_posted 	= validated_data.get('date_posted', instance.date_posted)

#  		instance.save()
#  		return instance
 
 		




