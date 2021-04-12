from django.test import SimpleTestCase, TestCase
from django.contrib.auth import get_user_model
from .models import Courses


class WebsiteTest(TestCase):
	# User Registration 
	username 		= 'codingrev'
	email 	 		= 'codingrev@gmail.com'
	password 		= 'thethethe'

	# Courses Post 
	tutor 			= get_user_model().objects.get(id=1)
	tutor			= tutor.id
	title 			= "Python Crash Course"
	price 			= "500"
	duration 		= "2"

	# Test for User Registration.
	def test_signup_process(self):
		user = get_user_model().objects.create_user(
										username = self.username, email=self.email,
										password=self.password,
										)
		self.assertEqual(get_user_model().objects.all().count(), 1)
		
		self.assertEqual(get_user_model().objects.all() 
			[0].username, self.username)

		self.assertEqual(get_user_model().objects.all() 
			[0].email, self.email)


	#Test for Posting Courses
	def post_test(self):
		new_course 		= Courses.objects.create(
										tutor = self.tutor, title=self.title,
										price = self.price, duration=self.duration
										)
		self.assertEqual(Courses().objects.all().count(), 1)

		self.assertEqual(Courses().objects.all() 
			[0].tutor, self.tutor)

		self.assertEqual(Courses().objects.all() 
			[0].title, self.title)

		self.assertEqual(Courses().objects.all() 
			[0].price, self.price)

		self.assertEqual(Courses().objects.all() 
			[0].duration, self.duration)





	
	

	
