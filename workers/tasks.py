import time
from celery import shared_task
from core.models import Video
from .models import ProcessingJOb

@shared_task
def VideoProcessingQueue():
    ProcessingJOb.status='PENDING'
    ProcessingJOb.save()
    time.sleep(10)
    ProcessingJOb.status='COMPLETED'
    ProcessingJOb.save()


