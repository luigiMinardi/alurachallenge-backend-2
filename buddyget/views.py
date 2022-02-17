from rest_framework import viewsets
from buddyget.models import Income, Expense
from buddyget.serializer import IncomeSerializer, ExpenseSerializer

class IncomesViewSet(viewsets.ModelViewSet):
    """Showing all incomes"""
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer

class ExpensesViewSet(viewsets.ModelViewSet):
    """Showing all expenses"""
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer