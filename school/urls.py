from django.urls import path

from .views import (
    CourseAPIView, 
    AssessmentAPIView,
    CourseOneAPIView
)     

urlpatterns = [
    path('courses', CourseAPIView.as_view(), name='courses'),
    path('courses/<int:pk>', CourseOneAPIView.as_view(), name='coursesone'),
    path('assessments', AssessmentAPIView.as_view(), name='assessments')
]