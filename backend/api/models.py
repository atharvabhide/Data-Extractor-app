from django.db import models
import uuid

class File(models.Model):
    uuid = models.UUIDField(blank=False, null=False, default=uuid.uuid4)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    file = models.FileField(upload_to='files/', blank=False, null=False)

    def __str__(self):
        return self.file.name