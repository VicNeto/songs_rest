from django.db import models
import uuid

class SongModel(models.Model):
    _id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(default="", max_length=50)
    artist = models.CharField(default="", max_length=100)
    duration = models.FloatField()

    class Meta:
        ordering = ['name']
