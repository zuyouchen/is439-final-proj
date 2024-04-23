from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from budget.models import (
    Advisor,
    Client,
    Expense,
    Income,
    Budget
)


class AdvisorList(ListView):
    model = Advisor


class AdvisorDetail(DetailView):
    model = Advisor

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        advisor = self.get_object()
        client_list = advisor.clients.all()
        context['advisor'] = advisor
        context['client_list'] = client_list
        return context


class ClientList(ListView):
    model = Client


class ClientDetail(DetailView):
    model = Client

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        client = self.get_object()
        expense_list = client.expenses.all()
        income_list = client.incomes.all()
        budget_list = client.budgets.all()
        context['client'] = client
        context['expense_list'] = expense_list
        context['income_list'] = income_list
        context['budget_list'] = budget_list
        return context


class ExpenseList(ListView):
    model = Expense


class ExpenseDetail(DetailView):
    model = Expense

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        expense = self.get_object()
        context['expense'] = expense
        return context


class IncomeList(ListView):
    model = Income


class IncomeDetail(DetailView):
    model = Income

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        income = self.get_object()
        context['income'] = income
        return context


class BudgetList(ListView):
    model = Budget


class BudgetDetail(DetailView):
    model = Budget

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        budget = self.get_object()
        budget_categories = budget.budget_categories.all()
        context['budget'] = budget
        context['budget_categories'] = budget_categories
        return context
