from django.contrib import admin
from .models import Courses

# Register your models here.
admin.site.site_title  = "Emmjoy Website"
admin.site.site_header = "Emmjoy Website"

admin.site.register(Courses)