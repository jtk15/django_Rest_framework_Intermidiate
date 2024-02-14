from rest_framework import serializers

from .models import Course, Assessment


class CourseSerializer(serializers.ModelSerializer):
    
    class Meta:
       
        model = Course
        fields  = ['id','title', 'url', 'criation', 'update', 'active']


class AssessmentSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = Assessment
        fields = ['id', 'course', 'email', 'score', 'comment', 'criation', 'update', 'active']