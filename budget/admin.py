from django.contrib import admin

from .models import Advisor, Client, ExpenseCategory, IncomeCategory, Frequency, Expense, Income, Budget, BudgetCategory

admin.site.register(Advisor)
admin.site.register(Client)
admin.site.register(ExpenseCategory)
admin.site.register(IncomeCategory)
admin.site.register(Frequency)
admin.site.register(Expense)
admin.site.register(Income)
admin.site.register(Budget)
admin.site.register(BudgetCategory)
