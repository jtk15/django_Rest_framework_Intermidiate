from django.contrib import admin

from .models import Course, Assessment


class AdminCourse(admin.ModelAdmin):
    
    list_display = ['title', 'url', 'criation', 'update', 'active']


class AdminAssesment(admin.ModelAdmin):
    
    list_display = ['course', 'email', 'score', 'criation', 'update', 'active', 'comment']

admin.site.register(Course, AdminCourse)
admin.site.register(Assessment, AdminAssesment)
