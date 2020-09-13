from django.contrib import admin
from budget.models.Aim import Aim
from budget.models.Budget import Budget
from budget.models.Income import Income
from budget.models.Expense import Expense


admin.site.register(Aim)
admin.site.register(Budget)
admin.site.register(Income)
admin.site.register(Expense)
