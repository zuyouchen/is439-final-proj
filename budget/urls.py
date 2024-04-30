from django.urls import path
from budget.views import (
    AdvisorList,
    ClientList,
    ExpenseList,
    IncomeList,
    BudgetList,
    AdvisorDetail,
    ClientDetail,
    ExpenseDetail,
    IncomeDetail,
    BudgetDetail,
    AdvisorCreate,
    ClientCreate,
    ExpenseCreate,
    IncomeCreate,
    BudgetCreate,
    BudgetCategoryCreate,
    AdvisorUpdate,
    ClientUpdate,
    ExpenseUpdate,
    IncomeUpdate,
    BudgetUpdate,
    BudgetCategoryUpdate,
    AdvisorDelete,
    ClientDelete,
    ExpenseDelete,
    IncomeDelete,
    BudgetDelete,
    BudgetCategoryDelete,
    FilterExpenseByCategory,
    FilterExpenseByFrequency,
    FilterIncomeByCategory,
    FilterIncomeByFrequency,
    VisualizeBudget
)

urlpatterns = [
    path('advisor/',
         AdvisorList.as_view(),
         name='budget_advisor_list_urlpattern'),

    path('advisor/<int:pk>/',
         AdvisorDetail.as_view(),
         name='budget_advisor_detail_urlpattern'),

    path('advisor/create/',
         AdvisorCreate.as_view(),
         name='budget_advisor_create_urlpattern'),

    path('advisor/<int:pk>/update/',
         AdvisorUpdate.as_view(),
         name='budget_advisor_update_urlpattern'),

    path('advisor/<int:pk>/delete/',
         AdvisorDelete.as_view(),
         name='budget_advisor_delete_urlpattern'),

    path('client/',
         ClientList.as_view(),
         name='budget_client_list_urlpattern'),

    path('client/<int:pk>/',
         ClientDetail.as_view(),
         name='budget_client_detail_urlpattern'),

    path('client/create/',
         ClientCreate.as_view(),
         name='budget_client_create_urlpattern'),

    path('client/<int:pk>/update/',
         ClientUpdate.as_view(),
         name='budget_client_update_urlpattern'),

    path('client/<int:pk>/delete/',
         ClientDelete.as_view(),
         name='budget_client_delete_urlpattern'),

    path('expense/',
         ExpenseList.as_view(),
         name='budget_expense_list_urlpattern'),

    path('expense/<int:pk>/',
         ExpenseDetail.as_view(),
         name='budget_expense_detail_urlpattern'),

    path('expense/create/',
         ExpenseCreate.as_view(),
         name='budget_expense_create_urlpattern'),

    path('expense/<int:pk>/update/',
         ExpenseUpdate.as_view(),
         name='budget_expense_update_urlpattern'),

    path('expense/<int:pk>/delete/',
         ExpenseDelete.as_view(),
         name='budget_expense_delete_urlpattern'),

    path('income/',
         IncomeList.as_view(),
         name='budget_income_list_urlpattern'),

    path('income/<int:pk>/',
         IncomeDetail.as_view(),
         name='budget_income_detail_urlpattern'),

    path('income/create/',
         IncomeCreate.as_view(),
         name='budget_income_create_urlpattern'),

    path('income/<int:pk>/update/',
         IncomeUpdate.as_view(),
         name='budget_income_update_urlpattern'),

    path('income/<int:pk>/delete/',
         IncomeDelete.as_view(),
         name='budget_income_delete_urlpattern'),

    path('budget/',
         BudgetList.as_view(),
         name='budget_budget_list_urlpattern'),

    path('budget/<int:pk>/',
         BudgetDetail.as_view(),
         name='budget_budget_detail_urlpattern'),

    path('budget/create/',
         BudgetCreate.as_view(),
         name='budget_budget_create_urlpattern'),

    path('budget/<int:pk>/update/',
         BudgetUpdate.as_view(),
         name='budget_budget_update_urlpattern'),

    path('budget/<int:pk>/delete/',
         BudgetDelete.as_view(),
         name='budget_budget_delete_urlpattern'),

    path('budgetcategory/create/',
         BudgetCategoryCreate.as_view(),
         name='budget_budget_category_create_urlpattern'),

    path('budgetcategory/<int:pk>/update/',
         BudgetCategoryUpdate.as_view(),
         name='budget_budget_category_update_urlpattern'),

    path('budgetcategory/<int:pk>/delete/',
         BudgetCategoryDelete.as_view(),
         name='budget_budget_category_delete_urlpattern'),

    path('expense/filter/category/',
         FilterExpenseByCategory.as_view(),
         name='budget_filter_expense_by_category_urlpattern'),

    path('expense/filter/frequency/',
         FilterExpenseByFrequency.as_view(),
         name='budget_filter_expense_by_frequency_urlpattern'),

    path('income/filter/category/',
         FilterIncomeByCategory.as_view(),
         name='budget_filter_income_by_category_urlpattern'),

    path('income/filter/frequency/',
         FilterIncomeByFrequency.as_view(),
         name='budget_filter_income_by_frequency_urlpattern'),

    path('budget/<int:pk>/visualize/',
         VisualizeBudget.as_view(),
         name='budget_budget_visualize_urlpattern'),

]
