from django.shortcuts import render
from register.models import EmmjoyUsers
from .models import Courses
from .serializers import RegistrationSerializer, CoursesSerializer
# API Class Based Imports
from rest_framework.views import APIView
# API Function Based Imports
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# ==================================
# Register API View
# ==================================
class RegisterAPIView(APIView):

	def get(self, request):
		user = EmmjoyUsers.objects.all()
		serializer = RegistrationSerializer(user, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = RegistrationSerializer(data=request.data)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegisterDetailView(APIView):

	def get_object(self, id):
		try:
			user = EmmjoyUsers.objects.get(id=id)
			return user

		except EmmjoyUsers.DoesNotExist:
			return HttpResponse(status=404)

	def get(self, request, id):
		user = self.get_object(id)
		serializer = RegistrationSerializer(user)
		return Response(serializer.data)


	def put(self, request, id):
		user = self.get_object(id)
		serializer = RegistrationSerializer(user, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_NOT_FOUND)


	def delete(self, request, id):
		user = self.get_object(id)
		user.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

# ==================================
# Post Course API View
# ==================================
@api_view(['GET', 'POST'])
def listCourses(request):

	if request.method == "GET":
		courses = Courses.objects.all()
		serializer = CoursesSerializer(courses, many=True)
		return Response(serializer.data)

	elif request.method =="POST":
		serializer = CoursesSerializer(data=request.data)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def detailCourse(request, pk):

	try:
		courses = Courses.objects.get(pk=pk)

	except BetSlips.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == "GET":
		serializer = CoursesSerializer(courses)
		return Response(serializer.data)

	elif request.method == 'PUT':
		serializer = CoursesSerializer(courses, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_NOT_FOUND)

	elif request.method == "DELETE":
		courses.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


