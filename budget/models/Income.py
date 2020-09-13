import uuid
from django.db import models
from budget.models.Budget import Budget


class Income(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    value = models.PositiveBigIntegerField()
    budget = models.ForeignKey(to=Budget, related_name='budgets', on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
