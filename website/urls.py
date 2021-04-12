from django.urls import path
from .views import *

app_name = "website"

urlpatterns =[
	path('registered-users', RegisterAPIView.as_view(), name='registered-users'),
    path('registered-users/<int:id>/', RegisterDetailView.as_view(), name="registered-user-detail"),
    
    path('courses', listCourses, name="courses"),
    path('courses/<int:pk>/', detailCourse, name="course-detail"),

]




