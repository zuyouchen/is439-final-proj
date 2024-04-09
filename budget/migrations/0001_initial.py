# Generated by Django 4.1 on 2024-04-09 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('budget_id', models.AutoField(primary_key=True, serialize=False)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('budget_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('client_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Frequency',
            fields=[
                ('frequency_id', models.AutoField(primary_key=True, serialize=False)),
                ('frequency_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('income_id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='incomes', to='budget.category')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='incomes', to='budget.client')),
                ('frequency', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='incomes', to='budget.frequency')),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('expense_id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='expenses', to='budget.category')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='expenses', to='budget.client')),
                ('frequency', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='expenses', to='budget.frequency')),
            ],
        ),
        migrations.CreateModel(
            name='BudgetCategory',
            fields=[
                ('budget_category_id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('budget', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='budget_categories', to='budget.budget')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='budget_categories', to='budget.category')),
            ],
        ),
        migrations.AddField(
            model_name='budget',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='budgets', to='budget.client'),
        ),
    ]
