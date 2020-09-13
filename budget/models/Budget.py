import uuid
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Budget(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(to=User, related_name='budgets', on_delete=models.CASCADE)
