from datetime import date

from django.test import TestCase

from budget.models.Aim import Aim
from budget.models.Budget import Budget
from budget.models.Expense import Expense
from budget.models.Income import Income

from django.contrib.auth import get_user_model

User = get_user_model()


class AimModelTest(TestCase):
    def test_aim_can_be_created(self):
        user = User.objects.create(username='admin', password='123')
        budget = Budget.objects.create(name='main', owner=user)
        date_now = date.today()

        Aim.objects.create(
            name='Buy a house',
            value=4_000_000,
            budget=budget,
            end_date=date_now
        )

        aim = Aim.objects.first()

        self.assertEqual(aim.name, 'Buy a house')
        self.assertEqual(aim.value, 4_000_000)
        self.assertEqual(aim.budget, budget)
        self.assertEqual(aim.end_date, date_now)


class BudgetModelTest(TestCase):
    pass


class ExpenseModelTest(TestCase):
    pass


class IncomeModelTest(TestCase):
    pass
