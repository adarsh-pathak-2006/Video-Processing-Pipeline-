from django.shortcuts import render
from .models import Video
from .serializers import VideoUploadSerializer
from rest_framework.generics import ListCreateAPIView

class VideoUploadAPI(ListCreateAPIView):
    queryset=Video.objects.all()
    serializer_class=VideoUploadSerializer

    def perform_create(self, serializer):
        serializer.save()