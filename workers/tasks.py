import time
from celery import shared_task
from core.models import Video
from .models import ProcessinJOb

@shared_task
def VideoProcessing()

