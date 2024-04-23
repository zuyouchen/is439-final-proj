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
)

urlpatterns = [
    path('advisor/',
         AdvisorList.as_view(),
         name='budget_advisor_list_urlpattern'),

    path('advisor/<int:pk>/',
         AdvisorDetail.as_view(),
         name='budget_advisor_detail_urlpattern'),

    path('client/',
         ClientList.as_view(),
         name='budget_client_list_urlpattern'),

    path('client/<int:pk>/',
         ClientDetail.as_view(),
         name='budget_client_detail_urlpattern'),

    path('expense/',
         ExpenseList.as_view(),
         name='budget_expense_list_urlpattern'),

    path('expense/<int:pk>/',
         ExpenseDetail.as_view(),
         name='budget_expense_detail_urlpattern'),

    path('income/',
         IncomeList.as_view(),
         name='budget_income_list_urlpattern'),

    path('income/<int:pk>/',
         IncomeDetail.as_view(),
         name='budget_income_detail_urlpattern'),

    path('budget/',
         BudgetList.as_view(),
         name='budget_budget_list_urlpattern'),

    path('budget/<int:pk>/',
         BudgetDetail.as_view(),
         name='budget_budget_detail_urlpattern'),

]
