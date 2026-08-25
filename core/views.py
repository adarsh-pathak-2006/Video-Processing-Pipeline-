from django.shortcuts import render
from .models import Video
from .serializers import VideoUploadSerializer
from rest_framework.generics import ListCreateAPIView
from workers.models import ProcessinJOb
from workers.tasks import VideoProcessing

class VideoUploadAPI(ListCreateAPIView):
    queryset=Video.objects.all()
    serializer_class=VideoUploadSerializer
    
    def perform_create(self, serializer):
        video = serializer.save()
        job = ProcessinJOb.objects.create(video=video, status='PENDING')
        VideoProcessing.delay(job.id)
