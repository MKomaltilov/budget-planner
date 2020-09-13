import uuid
from django.db import models
from budget.models.Budget import Budget


class Aim(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    value = models.PositiveBigIntegerField()
    budget = models.ForeignKey(to=Budget, related_name='aims', on_delete=models.CASCADE)
    end_date = models.DateField()
