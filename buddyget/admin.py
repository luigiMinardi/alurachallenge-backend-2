from django.contrib import admin

from buddyget.models import Income, Expense

class Incomes(admin.ModelAdmin):
    list_display = ('id', 'description', 'value', 'date')
    list_display_links = ('id', 'value', 'description')
    search_fields = ('description', 'date')
    list_per_page = 20

admin.site.register(Income, Incomes)

class Expenses(admin.ModelAdmin):
    list_display = ('id', 'description', 'value', 'date')
    list_display_links = ('id', 'value', 'description')
    search_fields = ('description', 'date')
    list_per_page = 20

admin.site.register(Expense, Expenses)