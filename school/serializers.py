from rest_framework import serializers

from .models import Course, Assessment


class CourseSerializer(serializers.ModelSerealizer):
    
    class Meta:
       
        model = Course
        fields  = ['title', 'url', 'creation', 'update', 'active']


class AssessmentSerializer(serializers.ModelSerealizer):
    
    class Meta:
        
        model = Assessment
        fields = ['course', 'email', 'score', 'comment', 'creation', 'update', 'active']