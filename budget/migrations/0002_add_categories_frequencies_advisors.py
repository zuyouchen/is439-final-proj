from django.db import migrations

# Data to be added to the database
EXPENSE_CATEGORIES = [
    "Housing",
    "Utilities",
    "Transportation",
    "Groceries",
    "Insurance",
    "Entertainment",
    "Clothing",
    "Education",
    "Fitness",
    "Dining Out",
    "Subscriptions",
    "Gifts",
    "Miscellaneous"
]

INCOME_CATEGORIES = [
    "Salary",
    "Freelance",
    "Investment",
    "Scholarship",
    "Miscellaneous"
]

FREQUENCIES = [
    "One-time",
    "Daily",
    "Weekly",
    "Monthly",
    "Annually",
    "Semesterly",
    "Bi-weekly"
]

FINANCIAL_ADVISORS = [
    {"first_name": "Harvey", "last_name": "Specter"},
    {"first_name": "Louis", "last_name": "Litt"},
    {"first_name": "Jessica", "last_name": "Pearson"},
    {"first_name": "Daniel", "last_name": "Hardman"}
]


def add_expense_categories(apps, schema_editor):
    expense_category = apps.get_model("budget", "ExpenseCategory")
    for category in EXPENSE_CATEGORIES:
        expense_category.objects.create(expense_category_name=category)


def add_income_categories(apps, schema_editor):
    income_category = apps.get_model("budget", "IncomeCategory")
    for category in INCOME_CATEGORIES:
        income_category.objects.create(income_category_name=category)


def add_frequencies(apps, schema_editor):
    frequency = apps.get_model("budget", "Frequency")
    for f in FREQUENCIES:
        frequency.objects.create(frequency_name=f)


def add_financial_advisors(apps, schema_editor):
    financial_advisor = apps.get_model("budget", "Advisor")
    for advisor in FINANCIAL_ADVISORS:
        financial_advisor.objects.create(
            first_name=advisor["first_name"],
            last_name=advisor["last_name"]
        )


def remove_expense_categories(apps, schema_editor):
    expense_category = apps.get_model("budget", "ExpenseCategory")
    for category in EXPENSE_CATEGORIES:
        instance = expense_category.objects.get(expense_category_name=category)
        instance.delete()


def remove_income_categories(apps, schema_editor):
    income_category = apps.get_model("budget", "IncomeCategory")
    for category in INCOME_CATEGORIES:
        instance = income_category.objects.get(income_category_name=category)
        instance.delete()


def remove_frequencies(apps, schema_editor):
    frequency = apps.get_model("budget", "Frequency")
    for f in FREQUENCIES:
        instance = frequency.objects.get(frequency_name=f)
        instance.delete()


def remove_financial_advisors(apps, schema_editor):
    financial_advisor = apps.get_model("budget", "Advisor")
    for advisor in FINANCIAL_ADVISORS:
        instance = financial_advisor.objects.get(
            first_name=advisor["first_name"],
            last_name=advisor["last_name"]
        )
        instance.delete()


class Migration(migrations.Migration):
    dependencies = [("budget", "0001_initial")]

    operations = [
        migrations.RunPython(
            code=add_expense_categories,
            reverse_code=remove_expense_categories,
        ),
        migrations.RunPython(
            code=add_income_categories,
            reverse_code=remove_income_categories,
        ),
        migrations.RunPython(
            code=add_frequencies,
            reverse_code=remove_frequencies,
        ),
        migrations.RunPython(
            code=add_financial_advisors,
            reverse_code=remove_financial_advisors,
        ),
    ]
