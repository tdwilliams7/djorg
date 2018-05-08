from uuid import uuid4
from django.db import models

# Create your mod


class Bookmark(models.Model):
    url = models.URLField('URL', unique=True)
    name = models.CharField(max_length=200)
    notes = models.TextField(blank=True)
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    def __str__(self):
        return self.name
