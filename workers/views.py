from django.shortcuts import render
from .serializers import ProcessingJObSerializer
from .models import ProcessinJOb
from rest_framework.generics import ListAPIView, RetrieveAPIView

class ProcessingJobAPI(ListAPIView):
    queryset=ProcessinJOb.objects.all()
    serializer_class=ProcessingJObSerializer

class ProcessingJobDetailAPI(RetrieveAPIView):
    queryset=ProcessinJOb.objects.all()
    serializer_class=ProcessingJObSerializer
