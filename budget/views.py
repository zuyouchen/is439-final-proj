from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from budget.models import (
    Advisor,
    Client,
    Expense,
    Income,
    Budget,
    BudgetCategory,
    ExpenseCategory,
    IncomeCategory,
    Frequency
)

from budget.forms import (
    AdvisorForm,
    ClientForm,
    ExpenseCreateForm,
    ExpenseUpdateForm,
    IncomeCreateForm,
    IncomeUpdateForm,
    BudgetForm,
    BudgetCategoryCreateForm,
    BudgetCategoryUpdateForm
)


class AdvisorList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Advisor
    permission_required = 'budget.view_advisor'


class AdvisorDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Advisor
    permission_required = 'budget.view_advisor'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        advisor = self.get_object()
        client_list = advisor.clients.all()
        context['advisor'] = advisor
        context['client_list'] = client_list
        return context


class AdvisorCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = AdvisorForm
    model = Advisor
    permission_required = 'budget.add_advisor'


class AdvisorUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = AdvisorForm
    model = Advisor
    template_name = 'budget/advisor_form_update.html'
    permission_required = 'budget.change_advisor'


class AdvisorDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Advisor
    success_url = reverse_lazy('budget_advisor_list_urlpattern')
    permission_required = 'budget.delete_advisor'

    def get(self, request, pk):
        advisor = get_object_or_404(Advisor, pk=pk)
        clients = advisor.clients.all()
        if clients.count() > 0:
            return render(
                request,
                'budget/advisor_refuse_delete.html',
                {'advisor': advisor,
                 'clients': clients}
            )
        else:
            return render(
                request,
                'budget/advisor_confirm_delete.html',
                {'advisor': advisor}
            )


class ClientList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Client
    permission_required = 'budget.view_client'


class ClientDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Client
    permission_required = 'budget.view_client'

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


class ClientCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = ClientForm
    model = Client
    permission_required = 'budget.add_client'


class ClientUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = ClientForm
    model = Client
    template_name = 'budget/client_form_update.html'
    permission_required = 'budget.change_client'


class ClientDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('budget_client_list_urlpattern')
    permission_required = 'budget.delete_client'

    def get(self, request, pk):
        client = get_object_or_404(Client, pk=pk)
        expenses = client.expenses.all()
        incomes = client.incomes.all()
        budgets = client.budgets.all()
        if (expenses.count() + incomes.count() + budgets.count()) > 0:
            return render(
                request,
                'budget/client_refuse_delete.html',
                {'client': client,
                 'expenses': expenses,
                 'incomes': incomes,
                 'budgets': budgets}
            )
        else:
            return render(
                request,
                'budget/client_confirm_delete.html',
                {'client': client}
            )


class ExpenseList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Expense
    permission_required = 'budget.view_expense'


class ExpenseDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Expense
    permission_required = 'budget.view_expense'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        expense = self.get_object()
        context['expense'] = expense
        return context


class ExpenseCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = ExpenseCreateForm
    model = Expense
    permission_required = 'budget.add_expense'


class ExpenseUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = ExpenseUpdateForm
    model = Expense
    template_name = 'budget/expense_form_update.html'
    permission_required = 'budget.change_expense'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        client = self.object.client
        category = self.object.category
        context['client'] = client
        context['category'] = category
        return context


class ExpenseDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Expense
    success_url = reverse_lazy('budget_expense_list_urlpattern')
    permission_required = 'budget.delete_expense'


class IncomeList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Income
    permission_required = 'budget.view_income'


class IncomeDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Income
    permission_required = 'budget.view_income'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        income = self.get_object()
        context['income'] = income
        return context


class IncomeCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = IncomeCreateForm
    model = Income
    permission_required = 'budget.add_income'


class IncomeUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = IncomeUpdateForm
    model = Income
    template_name = 'budget/income_form_update.html'
    permission_required = 'budget.create_income'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        client = self.object.client
        category = self.object.category
        context['client'] = client
        context['category'] = category
        return context


class IncomeDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Income
    success_url = reverse_lazy('budget_income_list_urlpattern')
    permission_required = 'budget.delete_income'


class BudgetList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Budget
    permission_required = 'budget.view_budget'


class BudgetDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Budget
    permission_required = 'budget.view_budget'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        budget = self.get_object()
        budget_categories = budget.budget_categories.all()
        context['budget'] = budget
        context['budget_categories'] = budget_categories
        return context


class BudgetCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = BudgetForm
    model = Budget
    permission_required = 'budget.add_budget'


class BudgetUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = BudgetForm
    model = Budget
    template_name = 'budget/budget_form_update.html'
    permission_required = 'budget.change_budget'


class BudgetDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Budget
    success_url = reverse_lazy('budget_budget_list_urlpattern')
    permission_required = 'budget.delete_budget'


# We need the ability to C/U/D a BudgetCategory, but we don't list them because they are budget-specific
class BudgetCategoryCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = BudgetCategoryCreateForm
    model = BudgetCategory
    permission_required = 'budget.add_budgetcategory'

    def get_initial(self):
        initial = super().get_initial()
        budget_id = self.request.GET.get('budget_id')
        if budget_id:
            initial['budget'] = budget_id
        return initial

    def form_valid(self, form):
        budget_id = self.request.GET.get('budget_id')
        if budget_id:
            budget = Budget.objects.get(pk=budget_id)
            form.instance.budget = budget
        return super().form_valid(form)

    def get_success_url(self):
        budget_id = self.object.budget.pk
        return reverse_lazy('budget_budget_detail_urlpattern', kwargs={'pk': budget_id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        budget_id = self.request.GET.get('budget_id')
        budget = Budget.objects.get(pk=budget_id)
        context['budget'] = budget
        return context


class BudgetCategoryUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = BudgetCategoryUpdateForm
    model = BudgetCategory
    template_name = 'budget/budgetcategory_form_update.html'
    permission_required = 'budget.change_budgetcategory'

    def get_success_url(self):
        budget_id = self.object.budget.budget_id
        return reverse_lazy('budget_budget_detail_urlpattern', kwargs={'pk': budget_id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        budget_id = self.request.GET.get('budget_id')
        budget = Budget.objects.get(pk=budget_id)
        context['budget'] = budget
        return context


class BudgetCategoryDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = BudgetCategory
    permission_required = 'budget.delete_budgetcategory'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        budget_id = self.request.GET.get('budget_id')
        budget = Budget.objects.get(pk=budget_id)
        context['budget'] = budget
        return context

    def get_success_url(self):
        budget_id = self.object.budget.budget_id
        return reverse_lazy('budget_budget_detail_urlpattern', kwargs={'pk': budget_id})

# Complex Views - Past Default CRUD Operations


class FilterExpenseByCategory(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Expense
    template_name = 'budget/filter_expense_by_category.html'
    context_object_name = 'expenses'
    permission_required = 'budget.view_expense'

    def get_queryset(self):
        expense_category_id = self.request.GET.get('expense_category_id')
        if expense_category_id:
            return Expense.objects.filter(category_id=expense_category_id)
        return Expense.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        expense_category_id = self.request.GET.get('expense_category_id')
        #  Logic to support the selected category becoming the default form option
        if expense_category_id:
            category = ExpenseCategory.objects.get(pk=expense_category_id)
            context['selected_category'] = category
            context['categories'] = ExpenseCategory.objects.all().exclude(pk=expense_category_id)
        else:
            context['categories'] = ExpenseCategory.objects.all()
        return context


class FilterExpenseByFrequency(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Expense
    template_name = 'budget/filter_expense_by_frequency.html'
    context_object_name = 'expenses'
    permission_required = 'budget.view_expense'

    def get_queryset(self):
        expense_frequency_id = self.request.GET.get('expense_frequency_id')
        if expense_frequency_id:
            return Expense.objects.filter(frequency_id=expense_frequency_id)
        return Expense.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        expense_frequency_id = self.request.GET.get('expense_frequency_id')
        #  Logic to support the selected frequency becoming the default form option
        if expense_frequency_id:
            frequency = Frequency.objects.get(pk=expense_frequency_id)
            context['selected_frequency'] = frequency
            context['frequencies'] = Frequency.objects.all().exclude(pk=expense_frequency_id)
        else:
            context['frequencies'] = Frequency.objects.all()
        return context


class FilterIncomeByCategory(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Income
    template_name = 'budget/filter_income_by_category.html'
    context_object_name = 'incomes'
    permission_required = 'budget.view_income'

    def get_queryset(self):
        income_category_id = self.request.GET.get('income_category_id')
        if income_category_id:
            return Income.objects.filter(category_id=income_category_id)
        return Income.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        income_category_id = self.request.GET.get('income_category_id')
        #  Logic to support the selected category becoming the default form option
        if income_category_id:
            category = IncomeCategory.objects.get(pk=income_category_id)
            context['selected_category'] = category
            context['categories'] = IncomeCategory.objects.all().exclude(pk=income_category_id)
        else:
            context['categories'] = IncomeCategory.objects.all()
        return context


class FilterIncomeByFrequency(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Income
    template_name = 'budget/filter_income_by_frequency.html'
    context_object_name = 'incomes'
    permission_required = 'budget.view_income'

    def get_queryset(self):
        income_frequency_id = self.request.GET.get('income_frequency_id')
        if income_frequency_id:
            return Income.objects.filter(frequency_id=income_frequency_id)
        return Income.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        income_frequency_id = self.request.GET.get('income_frequency_id')
        #  Logic to support the selected frequency becoming the default form option
        if income_frequency_id:
            frequency = Frequency.objects.get(pk=income_frequency_id)
            context['selected_frequency'] = frequency
            context['frequencies'] = Frequency.objects.all().exclude(pk=income_frequency_id)
        else:
            context['frequencies'] = Frequency.objects.all()
        return context


class VisualizeBudget(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    template_name = 'budget/visualize_budget.html'
    permission_required = 'budget.view_budget'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        budget_id = self.kwargs.get('pk')
        budget = Budget.objects.get(pk=budget_id)
        budget_categories = budget.budget_categories.all()

        labels = [category.category.expense_category_name for category in budget_categories]
        amounts = [float(category.amount) for category in budget_categories]

        context['labels'] = labels
        context['amounts'] = amounts
        context['budget'] = budget
        return context
