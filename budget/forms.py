from django import forms

from budget.models import (
    Advisor,
    Client,
    Expense,
    Income,
    Budget,
    BudgetCategory
)


class AdvisorForm(forms.ModelForm):
    class Meta:
        model = Advisor
        fields = '__all__'

    def clean_first_name(self):
        return self.cleaned_data['first_name'].strip()

    def clean_last_name(self):
        return self.cleaned_data['last_name'].strip()


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

    def clean_first_name(self):
        return self.cleaned_data['first_name'].strip()

    def clean_last_name(self):
        return self.cleaned_data['last_name'].strip()


class ExpenseCreateForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'

    def clean_description(self):
        return self.cleaned_data['description'].strip()


class ExpenseUpdateForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['amount', 'description', 'frequency', 'date']

    def clean_description(self):
        return self.cleaned_data['description'].strip()


class IncomeCreateForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = '__all__'

    def clean_description(self):
        return self.cleaned_data['description'].strip()


class IncomeUpdateForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['amount', 'description', 'frequency', 'date']

    def clean_description(self):
        return self.cleaned_data['description'].strip()


class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = '__all__'

    def clean_budget_name(self):
        return self.cleaned_data['budget_name'].strip()


class BudgetCategoryCreateForm(forms.ModelForm):
    class Meta:
        model = BudgetCategory
        fields = ['category', 'amount', 'budget']

    def __init__(self, *args, **kwargs):
        budget_id = kwargs.pop('budget_id', None)
        super().__init__(*args, **kwargs)
        self.fields['budget'].widget = forms.HiddenInput()  # hide budget selection from user

        if budget_id:
            self.fields['budget'].initial = budget_id


class BudgetCategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = BudgetCategory
        fields = ['category', 'amount', 'budget']

    def __init__(self, *args, **kwargs):
        budget_id = kwargs.pop('budget_id', None)
        super().__init__(*args, **kwargs)
        self.fields['budget'].widget = forms.HiddenInput()  # hide budget selection from user
        self.fields['category'].widget = forms.HiddenInput()  # hide category selection from user

        if budget_id:
            self.fields['budget'].initial = budget_id
