from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class User(AbstractUser):
    uuid = models.UUIDField(blank=False, null=False, default=uuid.uuid4)
    email = models.EmailField(max_length=254, unique=True)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = "User"

class File(models.Model):
    uuid = models.UUIDField(blank=False, null=False, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='files')
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    file = models.FileField(upload_to='files/', blank=False, null=False)

    def __str__(self):
        return self.file.name