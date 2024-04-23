# Generated by Django 4.1 on 2024-04-23 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advisor',
            fields=[
                ('advisor_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Financial Advisor',
                'verbose_name_plural': 'Financial Advisors',
            },
        ),
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('budget_id', models.AutoField(primary_key=True, serialize=False)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('budget_name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Budget',
                'verbose_name_plural': 'Budgets',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('client_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('advisor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='advisor', to='budget.advisor')),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
            },
        ),
        migrations.CreateModel(
            name='ExpenseCategory',
            fields=[
                ('expense_category_id', models.AutoField(primary_key=True, serialize=False)),
                ('expense_category_name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Expense Category',
                'verbose_name_plural': 'Expense Categories',
            },
        ),
        migrations.CreateModel(
            name='Frequency',
            fields=[
                ('frequency_id', models.AutoField(primary_key=True, serialize=False)),
                ('frequency_name', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Frequency',
                'verbose_name_plural': 'Frequencies',
            },
        ),
        migrations.CreateModel(
            name='IncomeCategory',
            fields=[
                ('income_category_id', models.AutoField(primary_key=True, serialize=False)),
                ('income_category_name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Income Category',
                'verbose_name_plural': 'Income Categories',
            },
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('income_id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='incomes', to='budget.incomecategory')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='incomes', to='budget.client')),
                ('frequency', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='incomes', to='budget.frequency')),
            ],
            options={
                'verbose_name': 'Income',
                'verbose_name_plural': 'Incomes',
            },
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('expense_id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='expenses', to='budget.expensecategory')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='expenses', to='budget.client')),
                ('frequency', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='expenses', to='budget.frequency')),
            ],
            options={
                'verbose_name': 'Expense',
                'verbose_name_plural': 'Expenses',
            },
        ),
        migrations.CreateModel(
            name='BudgetCategory',
            fields=[
                ('budget_category_id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('budget', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='budget_categories', to='budget.budget')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='budget_categories', to='budget.expensecategory')),
            ],
            options={
                'verbose_name': 'Budget Category',
                'verbose_name_plural': 'Budget Categories',
            },
        ),
        migrations.AddField(
            model_name='budget',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='budgets', to='budget.client'),
        ),
    ]
