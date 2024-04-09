from django.contrib import admin

from .models import Client, Category, Frequency, Expense, Income, Budget, BudgetCategory

admin.site.register(Client)
admin.site.register(Category)
admin.site.register(Frequency)
admin.site.register(Expense)
admin.site.register(Income)
admin.site.register(Budget)
admin.site.register(BudgetCategory)
