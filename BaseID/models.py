from django.db import models
import uuid

# Create your models here.
class baseIDModel(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created_by = models.DateTimeField(auto_now_add=True)
    updated_by = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True