from django.db import models


class Advisor(models.Model):
    advisor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    class Meta:
        verbose_name = "Financial Advisor"
        verbose_name_plural = "Financial Advisors"


class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    advisor = models.ForeignKey(Advisor, related_name='advisor', on_delete=models.PROTECT)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"


class ExpenseCategory(models.Model):
    expense_category_id = models.AutoField(primary_key=True)
    expense_category_name = models.CharField(max_length=255)

    def __str__(self):
        return '%s' % self.expense_category_name

    class Meta:
        verbose_name = "Expense Category"
        verbose_name_plural = "Expense Categories"


class IncomeCategory(models.Model):
    income_category_id = models.AutoField(primary_key=True)
    income_category_name = models.CharField(max_length=255)

    def __str__(self):
        return '%s' % self.income_category_name

    class Meta:
        verbose_name = "Income Category"
        verbose_name_plural = "Income Categories"


class Frequency(models.Model):
    frequency_id = models.AutoField(primary_key=True)
    frequency_name = models.CharField(max_length=20)

    def __str__(self):
        return '%s' % self.frequency_name

    class Meta:
        verbose_name = "Frequency"
        verbose_name_plural = "Frequencies"


class Expense(models.Model):
    expense_id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, related_name='expenses', on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)
    date = models.DateField()
    frequency = models.ForeignKey(Frequency, related_name='expenses', on_delete=models.PROTECT)
    category = models.ForeignKey(ExpenseCategory, related_name='expenses', on_delete=models.PROTECT)

    def __str__(self):
        return '%s - $%s (%s, %s)' % (self.client, self.amount, self.category, self.frequency)

    class Meta:
        verbose_name = "Expense"
        verbose_name_plural = "Expenses"


class Income(models.Model):
    income_id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, related_name='incomes', on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)
    date = models.DateField()
    frequency = models.ForeignKey(Frequency, related_name='incomes', on_delete=models.PROTECT)
    category = models.ForeignKey(IncomeCategory, related_name='incomes', on_delete=models.PROTECT)

    def __str__(self):
        return '%s - $%s (%s, %s)' % (self.client, self.amount, self.category, self.frequency)

    class Meta:
        verbose_name = "Income"
        verbose_name_plural = "Incomes"


class Budget(models.Model):
    budget_id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, related_name='budgets', on_delete=models.PROTECT)
    start_date = models.DateField()
    end_date = models.DateField()
    budget_name = models.CharField(max_length=255)

    def __str__(self):
        return '%s (%s - %s)' % (self.client, self.start_date, self.end_date)

    class Meta:
        verbose_name = "Budget"
        verbose_name_plural = "Budgets"


class BudgetCategory(models.Model):
    budget_category_id = models.AutoField(primary_key=True)
    budget = models.ForeignKey(Budget, related_name='budget_categories', on_delete=models.PROTECT)
    # We will assume budgets only manage expenses
    category = models.ForeignKey(ExpenseCategory, related_name='budget_categories', on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str(self):
        return '%s - %s: $%s' % (self.budget, self.category, self.amount)

    class Meta:
        verbose_name = "Budget Category"
        verbose_name_plural = "Budget Categories"
