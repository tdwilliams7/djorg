from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4


class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    #api_enabled = models.BooleanField(default=True)
    # other fields to consider adding:
    # CharField with choices for Categories
    # hook up to bookmarks
    # FileField to upload file attachments
    # More sophisticated connection to user to allow sharing
