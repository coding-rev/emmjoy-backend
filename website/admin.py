from django.contrib import admin
from .models import Courses

# Register your models here.
admin.site.site_title  = "Emmjoy Website"
admin.site.site_header = "Emmjoy Website"


class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'price','duration', 'tutor']
    list_filter = ['date_posted', 'tutor']

admin.site.register(Courses, CourseAdmin)


