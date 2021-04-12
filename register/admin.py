from django.contrib import admin
from .models import EmmjoyUsers
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email','is_tutor', 'is_student']
    list_filter = ['is_student', 'is_tutor']
    


admin.site.register(EmmjoyUsers, UserAdmin)