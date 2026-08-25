from django.urls import path
from .views import VideoUploadAPI

urlpatterns = [
    path('upload/', VideoUploadAPI.as_view(), name='video-upload'),
]
