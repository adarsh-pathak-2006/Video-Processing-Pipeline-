from rest_framework.serializers import ModelSerializer
from .models import ProcessinJOb

class ProcessingJObSerializer(ModelSerializer):
    class Meta:
        model=ProcessinJOb
        fields='__all__'