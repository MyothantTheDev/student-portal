from django.db import models
from embed_video.fields import EmbedVideoField
# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length=100)
    added = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=100, null=True)
    url = EmbedVideoField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-added']