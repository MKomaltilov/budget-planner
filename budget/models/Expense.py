import uuid
from datetime import date
from django.db import models
from budget.models.Aim import Aim
from budget.models.Budget import Budget


class Expense(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    value = models.PositiveBigIntegerField()
    description = models.TextField(max_length=500, default='')
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(null=True, blank=True)
    budget = models.ForeignKey(to=Budget, related_name='expenses', on_delete=models.CASCADE)
    aim = models.ForeignKey(to=Aim, related_name='expenses', on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
