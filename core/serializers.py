from rest_framework.serializers import ModelSerializer
from .models import Video

class VideoUploadSerializer(ModelSerializer):
    class Meta:
        model=Video
        fields='__all__'
        read_only_fields=['uploaded_on']