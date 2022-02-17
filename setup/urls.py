from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from buddyget.views import ExpensesViewSet, IncomesViewSet

router = routers.DefaultRouter()
router.register('expenses', ExpensesViewSet, basename='Expenses')
router.register('incomes', IncomesViewSet, basename='Incomes')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
