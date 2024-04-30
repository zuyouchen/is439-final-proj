from __future__ import unicode_literals
from itertools import chain

from django.db import migrations


def populate_permissions_lists(apps):
    permission_class = apps.get_model('auth', 'Permission')
    advisor_permissions = permission_class.objects.filter(content_type__app_label='budget',
                                                          content_type__model='advisor')

    client_permissions = permission_class.objects.filter(content_type__app_label='budget',
                                                         content_type__model='client')

    expense_category_permissions = permission_class.objects.filter(content_type__app_label='budget',
                                                                   content_type__model='expensecategory')

    income_category_permissions = permission_class.objects.filter(content_type__app_label='budget',
                                                                  content_type__model='incomecategory')

    frequency_permissions = permission_class.objects.filter(content_type__app_label='budget',
                                                            content_type__model='frequency')

    expense_permissions = permission_class.objects.filter(content_type__app_label='budget',
                                                          content_type__model='expense')

    income_permissions = permission_class.objects.filter(content_type__app_label='budget',
                                                         content_type__model='income')

    budget_permissions = permission_class.objects.filter(content_type__app_label='budget',
                                                         content_type__model='budget')

    budget_category_permissions = permission_class.objects.filter(content_type__app_label='budget',
                                                                  content_type__model='budgetcategory')

    perm_view_advisor = permission_class.objects.filter(content_type__app_label='budget',
                                                        content_type__model='advisor',
                                                        codename='view_advisor')

    perm_view_client = permission_class.objects.filter(content_type__app_label='budget',
                                                       content_type__model='client',
                                                       codename='view_client')

    perm_view_expense_category = permission_class.objects.filter(content_type__app_label='budget',
                                                                 content_type__model='expensecategory',
                                                                 codename='view_expensecategory')

    perm_view_income_category = permission_class.objects.filter(content_type__app_label='budget',
                                                                content_type__model='incomecategory',
                                                                codename='view_incomecategory')

    perm_view_frequency = permission_class.objects.filter(content_type__app_label='budget',
                                                  content_type__model='frequency',
                                                  codename='view_frequency')

    perm_view_expense = permission_class.objects.filter(content_type__app_label='budget',
                                                        content_type__model='expense',
                                                        codename='view_expense')

    perm_view_income = permission_class.objects.filter(content_type__app_label='budget',
                                                       content_type__model='income',
                                                       codename='view_income')

    perm_view_budget = permission_class.objects.filter(content_type__app_label='budget',
                                                       content_type__model='budget',
                                                       codename='view_budget')

    perm_view_budget_category = permission_class.objects.filter(content_type__app_label='budget',
                                                                content_type__model='budgetcategory',
                                                                codename='view_budgetcategory')

    business_technician_permissions = chain(advisor_permissions,
                                            client_permissions,
                                            expense_category_permissions,
                                            income_category_permissions,
                                            frequency_permissions,
                                            perm_view_expense,
                                            perm_view_income,
                                            perm_view_budget,
                                            perm_view_budget_category)

    financial_advisor_permissions = chain(perm_view_advisor,
                                          client_permissions,
                                          perm_view_expense_category,
                                          perm_view_income_category,
                                          perm_view_frequency,
                                          expense_permissions,
                                          income_permissions,
                                          budget_permissions,
                                          budget_category_permissions)

    business_client_permissions = chain(perm_view_advisor,
                                        perm_view_client,
                                        perm_view_expense_category,
                                        perm_view_income_category,
                                        perm_view_frequency,
                                        expense_permissions,
                                        income_permissions,
                                        budget_permissions,
                                        budget_category_permissions)

    my_groups_initialization_list = [
        {
            "name": "business_technician",
            "permissions_list": business_technician_permissions,
        },
        {
            "name": "financial_advisor",
            "permissions_list": financial_advisor_permissions,
        },
        {
            "name": "business_client",
            "permissions_list": business_client_permissions,
        },
    ]
    return my_groups_initialization_list


def add_group_permissions_data(apps, schema_editor):
    groups_initialization_list = populate_permissions_lists(apps)

    group_model_class = apps.get_model('auth', 'Group')
    for group in groups_initialization_list:
        if group['permissions_list'] is not None:
            group_object = group_model_class.objects.get(
                name=group['name']
            )
            group_object.permissions.set(group['permissions_list'])
            group_object.save()


def remove_group_permissions_data(apps, schema_editor):
    groups_initialization_list = populate_permissions_lists(apps)

    group_model_class = apps.get_model('auth', 'Group')
    for group in groups_initialization_list:
        if group['permissions_list'] is not None:
            group_object = group_model_class.objects.get(
                name=group['name']
            )
            list_of_permissions = group['permissions_list']
            for permission in list_of_permissions:
                group_object.permissions.remove(permission)
                group_object.save()


class Migration(migrations.Migration):
    dependencies = [
        ('budget', '0004_create_groups'),
    ]

    operations = [
        migrations.RunPython(
            add_group_permissions_data,
            remove_group_permissions_data
        )
    ]
