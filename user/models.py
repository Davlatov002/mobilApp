from django.db import models
import uuid

class Profile(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    email = models.EmailField(max_length=200, blank=False, null=False)
    password = models.CharField(max_length=200, blank=False, null=False)
    username = models.CharField(max_length=200, blank=False, null=False)
    name = models.CharField(max_length=200, blank=True, null=True)
    surname = models.CharField(max_length=250, blank=True, null=True)
    profile_image = models.TextField(null=True, blank=True)
    referal_link = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    is_archived = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return self.username
