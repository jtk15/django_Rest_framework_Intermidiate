from rest_framework import generics

from .models import Course, Assessment
from .serializers import CourseSerializer, AssessmentSerializer


class CourseAPIView(generics.ListCreateAPIView):
    
    queryset = Course.objects.all()
    serializer_class = CourseSerializer