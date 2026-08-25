import time
from celery import shared_task
from .models import ProcessinJOb

@shared_task
def VideoProcessing(job_id):
    try:
        job = ProcessinJOb.objects.get(id=job_id)
        job.status = 'PROCESSING'
        job.save()
        
        # Simulate background video processing
        time.sleep(5)
        
        job.status = 'COMPLETED'
        job.save()
    except ProcessinJOb.DoesNotExist:
        pass
