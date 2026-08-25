from django.urls import path
from .views import ProcessingJobAPI, ProcessingJobDetailAPI

urlpatterns = [
    path('jobs/', ProcessingJobAPI.as_view(), name='job-list'),
    path('jobs/<int:pk>/', ProcessingJobDetailAPI.as_view(), name='job-detail'),
]
