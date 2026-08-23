from django.db import models
from core.models import Video


class ProcessinJOb(models.Model):
    video=models.ForeignKey(Video, on_delete=models.CASCADE)
    status=models.CharField(max_length=10, choices=[('PENDING', 'PENDING'), ('PROCESSING', 'PROCESSING'), ('COMPLETED', 'COMPLETED')], default='PENDING')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.video.name
