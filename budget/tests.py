from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from budget.models import (
    Advisor,
    Client,
    ExpenseCategory,
    IncomeCategory,
    Frequency,
    Expense,
    Income,
    Budget,
    BudgetCategory,
)
from django.urls import reverse


# Test models.py string and get methods
class ModelTests(TestCase):
    def setUp(self):
        User.objects.create_superuser('test', 'test@example.com', 'pass')
        self.client.login(username='test', password='pass')
        self.income_category = IncomeCategory.objects.create(income_category_name='income-category')
        self.expense_category = ExpenseCategory.objects.create(expense_category_name='expense-category')
        self.frequency = Frequency.objects.create(frequency_name='frequency')
        self.advisor = Advisor.objects.create(first_name='test', last_name='advisor')
        self.client_obj = Client.objects.create(first_name='test', last_name='client', advisor=self.advisor)
        self.expense = Expense.objects.create(amount=100,
                                              description='test',
                                              category=self.expense_category,
                                              frequency=self.frequency,
                                              client=self.client_obj,
                                              date='9999-12-31')
        self.income = Income.objects.create(amount=100,
                                            description='test',
                                            category=self.income_category,
                                            frequency=self.frequency,
                                            client=self.client_obj,
                                            date='9999-12-31')
        self.budget = Budget.objects.create(client=self.client_obj,
                                            budget_name='test budget',
                                            start_date='9999-12-31',
                                            end_date='9999-12-31')
        self.budget_category = BudgetCategory.objects.create(budget=self.budget,
                                                             category=self.expense_category,
                                                             amount=100)

    def test_advisor_model(self):
        self.assertEqual(self.advisor.__str__(), 'test advisor')
        self.assertEqual(self.advisor.get_absolute_url(),
                         reverse('budget_advisor_detail_urlpattern', kwargs={'pk': self.advisor.pk}))
        self.assertEqual(self.advisor.get_update_url(),
                         reverse('budget_advisor_update_urlpattern', kwargs={'pk': self.advisor.pk}))
        self.assertEqual(self.advisor.get_delete_url(),
                         reverse('budget_advisor_delete_urlpattern', kwargs={'pk': self.advisor.pk}))

    def test_client_model(self):
        self.assertEqual(self.client_obj.__str__(), 'test client')
        self.assertEqual(self.client_obj.advisor, self.advisor)
        self.assertEqual(self.client_obj.get_absolute_url(),
                         reverse('budget_client_detail_urlpattern', kwargs={'pk': self.client_obj.pk}))
        self.assertEqual(self.client_obj.get_update_url(),
                         reverse('budget_client_update_urlpattern', kwargs={'pk': self.client_obj.pk}))
        self.assertEqual(self.client_obj.get_delete_url(),
                         reverse('budget_client_delete_urlpattern', kwargs={'pk': self.client_obj.pk}))

    def test_expense_category_model(self):
        self.assertEqual(self.expense_category.__str__(), 'expense-category')

    def test_income_category_model(self):
        self.assertEqual(self.income_category.__str__(), 'income-category')

    def test_frequency_model(self):
        self.assertEqual(self.frequency.__str__(), 'frequency')

    def test_expense_model(self):
        self.assertEqual(self.expense.__str__(), 'test client - $100 (expense-category, frequency)')
        self.assertEqual(self.expense.category, self.expense_category)
        self.assertEqual(self.expense.frequency, self.frequency)
        self.assertEqual(self.expense.get_absolute_url(),
                         reverse('budget_expense_detail_urlpattern', kwargs={'pk': self.expense.pk}))
        self.assertEqual(self.expense.get_update_url(),
                         reverse('budget_expense_update_urlpattern', kwargs={'pk': self.expense.pk}))
        self.assertEqual(self.expense.get_delete_url(),
                         reverse('budget_expense_delete_urlpattern', kwargs={'pk': self.expense.pk}))

    def test_income_model(self):
        self.assertEqual(self.income.__str__(), 'test client - $100 (income-category, frequency)')
        self.assertEqual(self.income.category, self.income_category)
        self.assertEqual(self.income.frequency, self.frequency)
        self.assertEqual(self.income.get_absolute_url(),
                         reverse('budget_income_detail_urlpattern', kwargs={'pk': self.income.pk}))
        self.assertEqual(self.income.get_update_url(),
                         reverse('budget_income_update_urlpattern', kwargs={'pk': self.income.pk}))
        self.assertEqual(self.income.get_delete_url(),
                         reverse('budget_income_delete_urlpattern', kwargs={'pk': self.income.pk}))

    def test_budget_model(self):
        self.assertEqual(self.budget.__str__(), 'test client - test budget')
        self.assertEqual(self.budget.client, self.client_obj)
        self.assertEqual(self.budget.get_absolute_url(),
                         reverse('budget_budget_detail_urlpattern', kwargs={'pk': self.budget.pk}))
        self.assertEqual(self.budget.get_update_url(),
                         reverse('budget_budget_update_urlpattern', kwargs={'pk': self.budget.pk}))
        self.assertEqual(self.budget.get_delete_url(),
                         reverse('budget_budget_delete_urlpattern', kwargs={'pk': self.budget.pk}))
        self.assertEqual(self.budget.get_visualize_url(),
                         reverse('budget_budget_visualize_urlpattern', kwargs={'pk': self.budget.pk}))

    def test_budget_category_model(self):
        self.assertEqual(self.budget_category.__str__(), 'test client - test budget - expense-category: $100')
        self.assertEqual(self.budget_category.budget, self.budget)
        self.assertEqual(self.budget_category.category, self.expense_category)
        self.assertEqual(self.budget_category.get_update_url(),
                         reverse('budget_budget_category_update_urlpattern',
                                 kwargs={'pk': self.budget_category.pk}))
        self.assertEqual(self.budget_category.get_delete_url(),
                         reverse('budget_budget_category_delete_urlpattern',
                                 kwargs={'pk': self.budget_category.pk}))


# Test that our URLs from urls.py resolve as expected
class URLTests(TestCase):
    def setUp(self):
        User.objects.create_superuser('test', 'test@example.com', 'pass')
        self.client.login(username='test', password='pass')
        self.income_category = IncomeCategory.objects.create(income_category_name='income-category')
        self.expense_category = ExpenseCategory.objects.create(expense_category_name='expense-category')
        self.frequency = Frequency.objects.create(frequency_name='frequency')
        self.advisor = Advisor.objects.create(first_name='test', last_name='advisor')
        self.client_obj = Client.objects.create(first_name='test', last_name='client', advisor=self.advisor)
        self.expense = Expense.objects.create(amount=100,
                                              description='test',
                                              category=self.expense_category,
                                              frequency=self.frequency,
                                              client=self.client_obj,
                                              date='9999-12-31')
        self.income = Income.objects.create(amount=100,
                                            description='test',
                                            category=self.income_category,
                                            frequency=self.frequency,
                                            client=self.client_obj,
                                            date='9999-12-31')
        self.budget = Budget.objects.create(client=self.client_obj,
                                            budget_name='test budget',
                                            start_date='9999-12-31',
                                            end_date='9999-12-31')
        self.budget_category = BudgetCategory.objects.create(budget=self.budget,
                                                             category=self.expense_category,
                                                             amount=100)

    def test_advisor_urls(self):
        advisor_list_url = reverse('budget_advisor_list_urlpattern')
        self.assertEqual(advisor_list_url, '/advisor/')
        advisor_detail_url = reverse('budget_advisor_detail_urlpattern', kwargs={'pk': self.advisor.pk})
        self.assertEqual(advisor_detail_url, f'/advisor/{self.advisor.pk}/')
        advisor_create_url = reverse('budget_advisor_create_urlpattern')
        self.assertEqual(advisor_create_url, f'/advisor/create/')
        advisor_update_url = reverse('budget_advisor_update_urlpattern', kwargs={'pk': self.advisor.pk})
        self.assertEqual(advisor_update_url, f'/advisor/{self.advisor.pk}/update/')
        advisor_delete_url = reverse('budget_advisor_delete_urlpattern', kwargs={'pk': self.advisor.pk})
        self.assertEqual(advisor_delete_url, f'/advisor/{self.advisor.pk}/delete/')

    def test_client_urls(self):
        client_list_url = reverse('budget_client_list_urlpattern')
        self.assertEqual(client_list_url, '/client/')
        client_detail_url = reverse('budget_client_detail_urlpattern', kwargs={'pk': self.client_obj.pk})
        self.assertEqual(client_detail_url, f'/client/{self.client_obj.pk}/')
        client_create_url = reverse('budget_client_create_urlpattern')
        self.assertEqual(client_create_url, '/client/create/')
        client_update_url = reverse('budget_client_update_urlpattern', kwargs={'pk': self.client_obj.pk})
        self.assertEqual(client_update_url, f'/client/{self.client_obj.pk}/update/')
        client_delete_url = reverse('budget_client_delete_urlpattern', kwargs={'pk': self.client_obj.pk})
        self.assertEqual(client_delete_url, f'/client/{self.client_obj.pk}/delete/')

    def test_expense_urls(self):
        expense_list_url = reverse('budget_expense_list_urlpattern')
        self.assertEqual(expense_list_url, '/expense/')
        expense_detail_url = reverse('budget_expense_detail_urlpattern', kwargs={'pk': self.expense.pk})
        self.assertEqual(expense_detail_url, f'/expense/{self.expense.pk}/')
        expense_create_url = reverse('budget_expense_create_urlpattern')
        self.assertEqual(expense_create_url, '/expense/create/')
        expense_update_url = reverse('budget_expense_update_urlpattern', kwargs={'pk': self.expense.pk})
        self.assertEqual(expense_update_url, f'/expense/{self.expense.pk}/update/')
        expense_delete_url = reverse('budget_expense_delete_urlpattern', kwargs={'pk': self.expense.pk})
        self.assertEqual(expense_delete_url, f'/expense/{self.expense.pk}/delete/')

    def test_income_urls(self):
        income_list_url = reverse('budget_income_list_urlpattern')
        self.assertEqual(income_list_url, '/income/')
        income_detail_url = reverse('budget_income_detail_urlpattern', kwargs={'pk': self.income.pk})
        self.assertEqual(income_detail_url, f'/income/{self.income.pk}/')
        income_create_url = reverse('budget_income_create_urlpattern')
        self.assertEqual(income_create_url, '/income/create/')
        income_update_url = reverse('budget_income_update_urlpattern', kwargs={'pk': self.income.pk})
        self.assertEqual(income_update_url, f'/income/{self.income.pk}/update/')
        income_delete_url = reverse('budget_income_delete_urlpattern', kwargs={'pk': self.income.pk})
        self.assertEqual(income_delete_url, f'/income/{self.income.pk}/delete/')

    def test_budget_urls(self):
        budget_list_url = reverse('budget_budget_list_urlpattern')
        self.assertEqual(budget_list_url, '/budget/')
        budget_detail_url = reverse('budget_budget_detail_urlpattern', kwargs={'pk': self.budget.pk})
        self.assertEqual(budget_detail_url, f'/budget/{self.budget.pk}/')
        budget_create_url = reverse('budget_budget_create_urlpattern')
        self.assertEqual(budget_create_url, '/budget/create/')
        budget_update_url = reverse('budget_budget_update_urlpattern', kwargs={'pk': self.budget.pk})
        self.assertEqual(budget_update_url, f'/budget/{self.budget.pk}/update/')
        budget_delete_url = reverse('budget_budget_delete_urlpattern', kwargs={'pk': self.budget.pk})
        self.assertEqual(budget_delete_url, f'/budget/{self.budget.pk}/delete/')

    def test_budget_category_urls(self):
        budget_category_create_url = reverse('budget_budget_category_create_urlpattern')
        self.assertEqual(budget_category_create_url, '/budgetcategory/create/')
        budget_category_update_url = reverse('budget_budget_category_update_urlpattern',
                                             kwargs={'pk': self.budget_category.pk})
        self.assertEqual(budget_category_update_url, f'/budgetcategory/{self.budget_category.pk}/update/')
        budget_category_delete_url = reverse('budget_budget_category_delete_urlpattern',
                                             kwargs={'pk': self.budget_category.pk})
        self.assertEqual(budget_category_delete_url, f'/budgetcategory/{self.budget_category.pk}/delete/')

    def test_filter_urls(self):
        filter_expense_by_category_url = reverse('budget_filter_expense_by_category_urlpattern')
        self.assertEqual(filter_expense_by_category_url, '/expense/filter/category/')
        filter_expense_by_frequency_url = reverse('budget_filter_expense_by_frequency_urlpattern')
        self.assertEqual(filter_expense_by_frequency_url, '/expense/filter/frequency/')
        filter_income_by_category_url = reverse('budget_filter_income_by_category_urlpattern')
        self.assertEqual(filter_income_by_category_url, '/income/filter/category/')
        filter_income_by_frequency_url = reverse('budget_filter_income_by_frequency_urlpattern')
        self.assertEqual(filter_income_by_frequency_url, '/income/filter/frequency/')

    def test_visualize_url(self):
        visualize_url = reverse('budget_budget_visualize_urlpattern', kwargs={'pk': self.budget.pk})
        self.assertEqual(visualize_url, f'/budget/{self.budget.pk}/visualize/')

    def test_misc_urls(self):
        home_url = reverse('home_urlpattern')
        self.assertEqual(home_url, '/home/')
        about_url = reverse('about_urlpattern')
        self.assertEqual(about_url, '/about/')
        login_url = reverse('login_urlpattern')
        self.assertEqual(login_url, '/login/')
        logout_url = reverse('logout_urlpattern')
        self.assertEqual(logout_url, '/logout/')


# Test each view in views.py, its response, and template used for rendering (not actual content)
class ViewsTests(TestCase):
    def setUp(self):
        User.objects.create_superuser('test', 'test@example.com', 'pass')
        self.client.login(username='test', password='pass')
        self.income_category = IncomeCategory.objects.create(income_category_name='income-category')
        self.expense_category = ExpenseCategory.objects.create(expense_category_name='expense-category')
        self.frequency = Frequency.objects.create(frequency_name='frequency')
        self.advisor = Advisor.objects.create(first_name='test', last_name='advisor')
        self.client_obj = Client.objects.create(first_name='test', last_name='client', advisor=self.advisor)
        self.expense = Expense.objects.create(amount=100,
                                              description='test',
                                              category=self.expense_category,
                                              frequency=self.frequency,
                                              client=self.client_obj,
                                              date='9999-12-31')
        self.income = Income.objects.create(amount=100,
                                            description='test',
                                            category=self.income_category,
                                            frequency=self.frequency,
                                            client=self.client_obj,
                                            date='9999-12-31')
        self.budget = Budget.objects.create(client=self.client_obj,
                                            budget_name='test budget',
                                            start_date='9999-12-31',
                                            end_date='9999-12-31')
        self.budget_category = BudgetCategory.objects.create(budget=self.budget,
                                                             category=self.expense_category,
                                                             amount=100)

    def test_home_view(self):
        get_home = self.client.get(reverse('home_urlpattern'))
        self.assertEqual(get_home.status_code, 200)
        self.assertTemplateUsed(get_home, 'budget/home.html')

    def test_login_view(self):
        get_login = self.client.get(reverse('login_urlpattern'))
        self.assertEqual(get_login.status_code, 200)
        self.assertTemplateUsed(get_login, 'budget/login.html')

    def test_logout_view(self):
        get_logout = self.client.get(reverse('logout_urlpattern'), follow=True)
        self.assertEqual(get_logout.status_code, 200)
        self.assertTemplateUsed(get_logout, 'budget/login.html')

    def test_about_view(self):
        get_about = self.client.get(reverse('about_urlpattern'))
        self.assertEqual(get_about.status_code, 200)
        self.assertTemplateUsed(get_about, 'budget/about.html')

    def test_list_views(self):
        for obj in ["advisor", "client", "expense", "income", "budget"]:
            get_obj_list = self.client.get(reverse(f'budget_{obj}_list_urlpattern'))
            self.assertEqual(get_obj_list.status_code, 200)
            self.assertTemplateUsed(get_obj_list, f'budget/{obj}_list.html')

    def test_detail_views(self):
        get_advisor_detail = self.client.get(reverse('budget_advisor_detail_urlpattern',
                                                     kwargs={'pk': self.advisor.pk}))
        get_client_detail = self.client.get(reverse('budget_client_detail_urlpattern',
                                                    kwargs={'pk': self.client_obj.pk}))
        get_expense_detail = self.client.get(reverse('budget_expense_detail_urlpattern',
                                                     kwargs={'pk': self.expense.pk}))
        get_income_detail = self.client.get(reverse('budget_income_detail_urlpattern',
                                                    kwargs={'pk': self.income.pk}))
        get_budget_detail = self.client.get(reverse('budget_budget_detail_urlpattern',
                                                    kwargs={'pk': self.budget.pk}))
        self.assertEqual(get_advisor_detail.status_code, 200)
        self.assertEqual(get_client_detail.status_code, 200)
        self.assertEqual(get_expense_detail.status_code, 200)
        self.assertEqual(get_income_detail.status_code, 200)
        self.assertEqual(get_budget_detail.status_code, 200)
        self.assertTemplateUsed(get_advisor_detail, 'budget/advisor_detail.html')
        self.assertTemplateUsed(get_client_detail, 'budget/client_detail.html')
        self.assertTemplateUsed(get_expense_detail, 'budget/expense_detail.html')
        self.assertTemplateUsed(get_income_detail, 'budget/income_detail.html')
        self.assertTemplateUsed(get_budget_detail, 'budget/budget_detail.html')

    def test_create_views(self):
        # GET the form to create an object
        for obj in ["advisor", "client", "expense", "income", "budget"]:
            get_obj_create = self.client.get(reverse(f'budget_{obj}_create_urlpattern'))
            self.assertEqual(get_obj_create.status_code, 200)
            self.assertTemplateUsed(get_obj_create, f'budget/{obj}_form.html')
        get_budget_category_create = self.client.get(f"%s?budget_id={self.budget.pk}" %
                                                     reverse('budget_budget_category_create_urlpattern'))
        self.assertEqual(get_budget_category_create.status_code, 200)
        self.assertTemplateUsed(get_budget_category_create, 'budget/budgetcategory_form.html')
        #  POST to create each particular object, should work and be redirected to detailed page
        post_create_advisor = self.client.post(reverse('budget_advisor_create_urlpattern'),
                                               data={'first_name': 'a', 'last_name': 'b'},
                                               follow=True)
        self.assertEqual(post_create_advisor.status_code, 200)
        self.assertTemplateUsed(post_create_advisor, 'budget/advisor_detail.html')
        post_create_client = self.client.post(reverse('budget_client_create_urlpattern'),
                                              data={'first_name': 'c', 'last_name': 'd', 'advisor': self.advisor.pk},
                                              follow=True)
        self.assertEqual(post_create_client.status_code, 200)
        self.assertTemplateUsed(post_create_client, 'budget/client_detail.html')
        post_create_expense = self.client.post(reverse('budget_expense_create_urlpattern'),
                                               data={'client': self.client_obj.pk,
                                                     'amount': 100,
                                                     'description': 'new',
                                                     'category': self.expense_category.pk,
                                                     'frequency': self.frequency.pk,
                                                     'date': '9999-12-31'},
                                               follow=True)
        self.assertEqual(post_create_expense.status_code, 200)
        self.assertTemplateUsed(post_create_expense, 'budget/expense_detail.html')
        post_create_income = self.client.post(reverse('budget_income_create_urlpattern'),
                                              data={'client': self.client_obj.pk,
                                                    'amount': 100,
                                                    'description': 'new',
                                                    'category': self.income_category.pk,
                                                    'frequency': self.frequency.pk,
                                                    'date': '9999-12-31'},
                                              follow=True)
        self.assertEqual(post_create_income.status_code, 200)
        self.assertTemplateUsed(post_create_income, 'budget/income_detail.html')
        post_create_budget = self.client.post(reverse('budget_budget_create_urlpattern'),
                                              data={'client': self.client_obj.pk,
                                                    'budget_name': 'new',
                                                    'start_date': '9999-12-31',
                                                    'end_date': '9999-12-31'},
                                              follow=True)
        self.assertEqual(post_create_budget.status_code, 200)
        self.assertTemplateUsed(post_create_budget, 'budget/budget_detail.html')
        post_create_budget_category = self.client.post(reverse('budget_budget_category_create_urlpattern'),
                                                       data={'budget': self.budget.pk,
                                                             'category': self.expense_category.pk,
                                                             'amount': 100},
                                                       follow=True)
        self.assertEqual(post_create_budget_category.status_code, 200)
        self.assertTemplateUsed(post_create_budget_category, 'budget/budget_detail.html')
        # Fetch the new objects we've made and cleanup the objects for other tests
        new_advisor = Advisor.objects.last()
        new_client = Client.objects.last()
        new_expense = Expense.objects.last()
        new_income = Income.objects.last()
        new_budget = Budget.objects.last()
        new_budget_category = BudgetCategory.objects.last()
        new_advisor.delete()
        new_client.delete()
        new_expense.delete()
        new_income.delete()
        new_budget.delete()
        new_budget_category.delete()

    def test_update_views(self):
        # GET the update form for each model
        get_update_advisor = self.client.get(reverse('budget_advisor_update_urlpattern',
                                                     kwargs={'pk': self.advisor.pk}))
        get_update_client = self.client.get(reverse('budget_client_update_urlpattern',
                                                    kwargs={'pk': self.client_obj.pk}))
        get_update_expense = self.client.get(reverse('budget_expense_update_urlpattern',
                                                     kwargs={'pk': self.expense.pk}))
        get_update_income = self.client.get(reverse('budget_income_update_urlpattern',
                                                    kwargs={'pk': self.income.pk}))
        get_update_budget = self.client.get(reverse('budget_budget_update_urlpattern',
                                                    kwargs={'pk': self.budget.pk}))
        get_update_budget_category = self.client.get(f"%s?budget_id={self.budget.pk}" %
                                                     reverse('budget_budget_category_update_urlpattern',
                                                             kwargs={'pk': self.budget_category.pk}))
        self.assertEqual(get_update_advisor.status_code, 200)
        self.assertEqual(get_update_client.status_code, 200)
        self.assertEqual(get_update_expense.status_code, 200)
        self.assertEqual(get_update_income.status_code, 200)
        self.assertEqual(get_update_budget.status_code, 200)
        self.assertEqual(get_update_budget_category.status_code, 200)
        self.assertTemplateUsed(get_update_advisor, 'budget/advisor_form_update.html')
        self.assertTemplateUsed(get_update_client, 'budget/client_form_update.html')
        self.assertTemplateUsed(get_update_expense, 'budget/expense_form_update.html')
        self.assertTemplateUsed(get_update_income, 'budget/income_form_update.html')
        self.assertTemplateUsed(get_update_budget, 'budget/budget_form_update.html')
        self.assertTemplateUsed(get_update_budget_category, 'budget/budgetcategory_form_update.html')
        # POST to actually update, and see if the update worked for the model
        self.assertEqual(self.advisor.first_name, 'test')
        post_update_advisor = self.client.post(reverse('budget_advisor_update_urlpattern',
                                               kwargs={'pk': self.advisor.pk}),
                                               data={'first_name': 'test-update', 'last_name': 'advisor'},
                                               follow=True)
        self.assertEqual(post_update_advisor.status_code, 200)
        self.assertTemplateUsed(post_update_advisor, 'budget/advisor_detail.html')
        self.advisor.refresh_from_db()
        self.assertEqual(self.advisor.first_name, 'test-update')

        self.assertEqual(self.client_obj.first_name, 'test')
        post_update_client = self.client.post(reverse('budget_client_update_urlpattern',
                                              kwargs={'pk': self.client_obj.pk}),
                                              data={'first_name': 'test-update',
                                                    'last_name': 'client',
                                                    'advisor': self.advisor.pk},
                                              follow=True)
        self.assertEqual(post_update_client.status_code, 200)
        self.assertTemplateUsed(post_update_client, 'budget/client_detail.html')
        self.client_obj.refresh_from_db()
        self.assertEqual(self.client_obj.first_name, 'test-update')

        self.assertEqual(self.income.amount, 100)
        post_update_income = self.client.post(reverse('budget_income_update_urlpattern',
                                                      kwargs={'pk': self.income.pk}),
                                              data={'amount': 101,
                                                    'description': 'test',
                                                    'category': self.income_category.pk,
                                                    'frequency': self.frequency.pk,
                                                    'client': self.client_obj.pk,
                                                    'date': '9999-12-31'},
                                              follow=True)
        self.assertEqual(post_update_income.status_code, 200)
        self.assertTemplateUsed(post_update_income, 'budget/income_detail.html')
        self.income.refresh_from_db()
        self.assertEqual(self.income.amount, 101)

        self.assertEqual(self.expense.amount, 100)
        post_update_expense = self.client.post(reverse('budget_expense_update_urlpattern',
                                                       kwargs={'pk': self.expense.pk}),
                                               data={'amount': 101,
                                                     'description': 'test',
                                                     'category': self.expense_category.pk,
                                                     'frequency': self.frequency.pk,
                                                     'client': self.client_obj.pk,
                                                     'date': '9999-12-31'},
                                               follow=True)
        self.assertEqual(post_update_expense.status_code, 200)
        self.assertTemplateUsed(post_update_expense, 'budget/expense_detail.html')
        self.expense.refresh_from_db()
        self.assertEqual(self.expense.amount, 101)

        self.assertEqual(self.budget.budget_name, 'test budget')
        post_update_budget = self.client.post(reverse('budget_budget_update_urlpattern',
                                                      kwargs={'pk': self.budget.pk}),
                                              data={'budget_name': 'test budget update',
                                                    'client': self.client_obj.pk,
                                                    'start_date': '9999-12-31',
                                                    'end_date': '9999-12-31'},
                                              follow=True)
        self.assertEqual(post_update_budget.status_code, 200)
        self.assertTemplateUsed(post_update_budget, 'budget/budget_detail.html')
        self.budget.refresh_from_db()
        self.assertEqual(self.budget.budget_name, 'test budget update')

        self.assertEqual(self.budget_category.amount, 100)
        post_update_budget_category = self.client.post(f"%s?budget_id={self.budget.pk}" %
                                                       reverse('budget_budget_category_update_urlpattern',
                                                               kwargs={'pk': self.budget_category.pk}),
                                                       data={'budget': self.budget.pk,
                                                             'category': self.expense_category.pk,
                                                             'amount': 101},
                                                       follow=True)
        self.assertEqual(post_update_budget_category.status_code, 200)
        self.assertTemplateUsed(post_update_budget_category, 'budget/budget_detail.html')
        self.budget_category.refresh_from_db()
        self.assertEqual(self.budget_category.amount, 101)

    def test_delete_views_refusal(self):
        get_delete_advisor = self.client.get(reverse('budget_advisor_delete_urlpattern',
                                                     kwargs={'pk': self.advisor.pk}))
        get_delete_client = self.client.get(reverse('budget_client_delete_urlpattern',
                                                    kwargs={'pk': self.client_obj.pk}))
        self.assertEqual(get_delete_advisor.status_code, 200)
        self.assertEqual(get_delete_client.status_code, 200)
        self.assertTemplateUsed(get_delete_advisor, 'budget/advisor_refuse_delete.html')
        self.assertTemplateUsed(get_delete_client, 'budget/client_refuse_delete.html')

    def test_delete_views_confirm(self):
        get_delete_expense = self.client.get(reverse('budget_expense_delete_urlpattern',
                                                     kwargs={'pk': self.expense.pk}))
        get_delete_income = self.client.get(reverse('budget_income_delete_urlpattern',
                                                    kwargs={'pk': self.income.pk}))
        get_delete_budget = self.client.get(reverse('budget_budget_delete_urlpattern',
                                                    kwargs={'pk': self.budget.pk}))
        get_delete_budget_category = self.client.get(f"%s?budget_id={self.budget.pk}" %
                                                     reverse('budget_budget_category_delete_urlpattern',
                                                             kwargs={'pk': self.budget_category.pk}))
        self.assertEqual(get_delete_expense.status_code, 200)
        self.assertEqual(get_delete_income.status_code, 200)
        self.assertEqual(get_delete_budget.status_code, 200)
        self.assertEqual(get_delete_budget_category.status_code, 200)
        self.assertTemplateUsed(get_delete_expense, 'budget/expense_confirm_delete.html')
        self.assertTemplateUsed(get_delete_income, 'budget/income_confirm_delete.html')
        self.assertTemplateUsed(get_delete_budget, 'budget/budget_confirm_delete.html')
        self.assertTemplateUsed(get_delete_budget_category, 'budget/budgetcategory_confirm_delete.html')

    def test_filter_views(self):
        get_expense_by_category = self.client.get(reverse('budget_filter_expense_by_category_urlpattern'))
        self.assertEqual(get_expense_by_category.status_code, 200)
        self.assertTemplateUsed(get_expense_by_category, 'budget/filter_expense_by_category.html')

        get_expense_by_frequency = self.client.get(reverse('budget_filter_expense_by_frequency_urlpattern'))
        self.assertEqual(get_expense_by_frequency.status_code, 200)
        self.assertTemplateUsed(get_expense_by_frequency, 'budget/filter_expense_by_frequency.html')

        get_income_by_category = self.client.get(reverse('budget_filter_income_by_category_urlpattern'))
        self.assertEqual(get_income_by_category.status_code, 200)
        self.assertTemplateUsed(get_income_by_category, 'budget/filter_income_by_category.html')

        get_income_by_frequency = self.client.get(reverse('budget_filter_income_by_frequency_urlpattern'))
        self.assertEqual(get_income_by_frequency.status_code, 200)
        self.assertTemplateUsed(get_income_by_frequency, 'budget/filter_income_by_frequency.html')

    def test_visualize_view(self):
        get_visualized_budget = self.client.get(reverse('budget_budget_visualize_urlpattern',
                                                        kwargs={'pk': self.budget.pk}))
        self.assertEqual(get_visualized_budget.status_code, 200)
        self.assertTemplateUsed(get_visualized_budget, 'budget/visualize_budget.html')

    def test_home_redirects(self):
        get_main = self.client.get('')
        self.assertEqual(get_main.status_code, 302)
        self.assertRedirects(get_main, reverse('home_urlpattern'))


# Test the content within particular templates, including navigation buttons
class TemplateTests(TestCase):
    def setUp(self):
        User.objects.create_superuser('test', 'test@example.com', 'pass')
        self.client.login(username='test', password='pass')
        self.income_category = IncomeCategory.objects.create(income_category_name='income-category')
        self.expense_category = ExpenseCategory.objects.create(expense_category_name='expense-category')
        self.frequency = Frequency.objects.create(frequency_name='frequency')
        self.advisor = Advisor.objects.create(first_name='test', last_name='advisor')
        self.client_obj = Client.objects.create(first_name='test', last_name='client', advisor=self.advisor)
        self.expense = Expense.objects.create(amount=100,
                                              description='test',
                                              category=self.expense_category,
                                              frequency=self.frequency,
                                              client=self.client_obj,
                                              date='9999-12-31')
        self.income = Income.objects.create(amount=100,
                                            description='test',
                                            category=self.income_category,
                                            frequency=self.frequency,
                                            client=self.client_obj,
                                            date='9999-12-31')
        self.budget = Budget.objects.create(client=self.client_obj,
                                            budget_name='test budget',
                                            start_date='9999-12-31',
                                            end_date='9999-12-31')
        self.budget_category = BudgetCategory.objects.create(budget=self.budget,
                                                             category=self.expense_category,
                                                             amount=100)

    def test_list_view_templates(self):
        get_advisor_list = self.client.get(reverse('budget_advisor_list_urlpattern'))
        get_client_list = self.client.get(reverse('budget_client_list_urlpattern'))
        get_expense_list = self.client.get(reverse('budget_expense_list_urlpattern'))
        get_income_list = self.client.get(reverse('budget_income_list_urlpattern'))
        get_budget_list = self.client.get(reverse('budget_budget_list_urlpattern'))
        self.assertContains(get_advisor_list,
                            f"<a class=\"button\" href=\"{reverse('budget_advisor_create_urlpattern')}\">"
                            "Create New Advisor</a>",
                            html=True)
        self.assertContains(get_advisor_list, self.advisor.__str__())
        self.assertContains(get_client_list,
                            f"<a class=\"button\" href=\"{reverse('budget_client_create_urlpattern')}\">"
                            "Create New Client</a>",
                            html=True)
        self.assertContains(get_client_list, self.client_obj.__str__())
        self.assertContains(get_expense_list,
                            f"<a class=\"button\" href=\"{reverse('budget_expense_create_urlpattern')}\">"
                            "Create New Expense</a>",
                            html=True)
        self.assertContains(get_expense_list, "test client - $100.00 (expense-category, frequency)")
        self.assertContains(get_income_list,
                            f"<a class=\"button\" href=\"{reverse('budget_income_create_urlpattern')}\">"
                            "Create New Income</a>",
                            html=True)
        self.assertContains(get_income_list, "test client - $100.00 (income-category, frequency)")
        self.assertContains(get_budget_list,
                            f"<a class=\"button\" href=\"{reverse('budget_budget_create_urlpattern')}\">"
                            "Create New Budget</a>",
                            html=True)
        self.assertContains(get_budget_list, self.budget.__str__())

    def test_detail_view_templates(self):
        get_advisor_detail = self.client.get(reverse('budget_advisor_detail_urlpattern',
                                                     kwargs={'pk': self.advisor.pk}))
        get_client_detail = self.client.get(reverse('budget_client_detail_urlpattern',
                                                    kwargs={'pk': self.client_obj.pk}))
        get_expense_detail = self.client.get(reverse('budget_expense_detail_urlpattern',
                                                     kwargs={'pk': self.expense.pk}))
        get_income_detail = self.client.get(reverse('budget_income_detail_urlpattern',
                                                    kwargs={'pk': self.income.pk}))
        get_budget_detail = self.client.get(reverse('budget_budget_detail_urlpattern',
                                                    kwargs={'pk': self.budget.pk}))
        self.assertContains(get_advisor_detail,
                            f"<a class=\"button\" href=\"{self.advisor.get_update_url()}\">Update Advisor</a>",
                            html=True)
        self.assertContains(get_advisor_detail,
                            f"<a class=\"button\" href=\"{self.advisor.get_delete_url()}\">Delete Advisor</a>",
                            html=True)
        self.assertContains(get_client_detail,
                            f"<a class=\"button\" href=\"{self.client_obj.get_update_url()}\">Update Client</a>",
                            html=True)
        self.assertContains(get_client_detail,
                            f"<a class=\"button\" href=\"{self.client_obj.get_delete_url()}\">Delete Client</a>",
                            html=True)
        self.assertContains(get_expense_detail,
                            f"<a class=\"button\" href=\"{self.expense.get_update_url()}\">Update Expense</a>",
                            html=True)
        self.assertContains(get_expense_detail,
                            f"<a class=\"button\" href=\"{self.expense.get_delete_url()}\">Delete Expense</a>",
                            html=True)
        self.assertContains(get_income_detail,
                            f"<a class=\"button\" href=\"{self.income.get_update_url()}\">Update Income</a>",
                            html=True)
        self.assertContains(get_income_detail,
                            f"<a class=\"button\" href=\"{self.income.get_delete_url()}\">Delete Income</a>",
                            html=True)
        self.assertContains(get_budget_detail,
                            f"<a class=\"button\" href=\"{self.budget.get_update_url()}\">Update Budget</a>",
                            html=True)
        self.assertContains(get_budget_detail,
                            f"<a class=\"button\" href=\"{self.budget.get_delete_url()}\">Delete Budget</a>",
                            html=True)

    # No need to test create or delete view templates, as their relevant content was tested by the assertTemplateUsed
    # in the tests contained in TestViews() class above

    def test_filter_view_templates(self):
        filter_expense_by_category_response = self.client.get(reverse('budget_filter_expense_by_category_urlpattern'),
                                                              data={'expense_category_id': self.expense_category.pk})
        self.assertEqual(filter_expense_by_category_response.status_code, 200)
        self.assertContains(filter_expense_by_category_response, "test client - $100.00 (expense-category, frequency)")
        filter_expense_by_frequency_response = self.client.get(reverse('budget_filter_expense_by_frequency_urlpattern'),
                                                               data={'expense_frequency_id': self.frequency.pk})
        self.assertEqual(filter_expense_by_frequency_response.status_code, 200)
        self.assertContains(filter_expense_by_frequency_response, "test client - $100.00 (expense-category, frequency)")

        filter_income_by_category_response = self.client.get(reverse('budget_filter_income_by_category_urlpattern'),
                                                             data={'income_category_id': self.income_category.pk})
        self.assertEqual(filter_income_by_category_response.status_code, 200)
        self.assertContains(filter_income_by_category_response, "test client - $100.00 (income-category, frequency)")
        filter_income_by_frequency_response = self.client.get(reverse('budget_filter_income_by_frequency_urlpattern'),
                                                              data={'income_frequency_id': self.frequency.pk})
        self.assertEqual(filter_income_by_frequency_response.status_code, 200)
        self.assertContains(filter_income_by_frequency_response, "test client - $100.00 (income-category, frequency)")

    def test_visualize_view_templates(self):
        visualize_budget_response = self.client.get(reverse('budget_budget_visualize_urlpattern',
                                                            kwargs={'pk': self.budget.pk}))
        self.assertEqual(visualize_budget_response.status_code, 200)
        self.assertContains(visualize_budget_response, "<h3>Bar Chart</h3>", html=True)
        self.assertContains(visualize_budget_response, "<h3>Pie Chart</h3>", html=True)


class LoginLogoutTests(TestCase):
    def setUp(self):
        User.objects.create_user(username="test", password="secret")

    def test_login_page(self):
        get_login_page = self.client.get(reverse('login_urlpattern'))
        self.assertTemplateUsed(get_login_page, 'budget/login.html')

    def test_login_functionality(self):
        response = self.client.post(reverse('login_urlpattern'),
                                    data={'username': 'test', 'password': 'secret'},
                                    follow=True)
        self.assertTrue(response.context['user'].is_authenticated)
        self.assertRedirects(response, reverse('home_urlpattern'))

    def test_logout_functionality(self):
        self.client.login(username='test', password='secret')
        response = self.client.get(reverse('logout_urlpattern'), follow=True)
        self.assertFalse(response.context['user'].is_authenticated)
        self.assertRedirects(response, reverse('login_urlpattern'))


class AuthenticationAuthorizationTests(TestCase):
    # For now, we test the superuser and non-superuser authentications.
    def setUp(self):
        User.objects.create_superuser(username='superuser', password='pass')
        User.objects.create_user(username='non-superuser', password='pass')

        self.income_category = IncomeCategory.objects.create(income_category_name='income-category')
        self.expense_category = ExpenseCategory.objects.create(expense_category_name='expense-category')
        self.frequency = Frequency.objects.create(frequency_name='frequency')
        self.advisor = Advisor.objects.create(first_name='test', last_name='advisor')
        self.client_obj = Client.objects.create(first_name='test', last_name='client', advisor=self.advisor)
        self.expense = Expense.objects.create(amount=100,
                                              description='test',
                                              category=self.expense_category,
                                              frequency=self.frequency,
                                              client=self.client_obj,
                                              date='9999-12-31')
        self.income = Income.objects.create(amount=100,
                                            description='test',
                                            category=self.income_category,
                                            frequency=self.frequency,
                                            client=self.client_obj,
                                            date='9999-12-31')
        self.budget = Budget.objects.create(client=self.client_obj,
                                            budget_name='test budget',
                                            start_date='9999-12-31',
                                            end_date='9999-12-31')
        self.budget_category = BudgetCategory.objects.create(budget=self.budget,
                                                             category=self.expense_category,
                                                             amount=100)

    # See: https://docs.djangoproject.com/en/5.0/topics/auth/default/#permission-caching
    @staticmethod
    def refresh_user(username):
        return get_object_or_404(User, username=username)

    def test_superuser(self):
        superuser = self.refresh_user('superuser')
        self.client.force_login(superuser)
        full_permission_objects = ['advisor', 'client', 'expense', 'income', 'budget', 'budget_category']
        for obj in full_permission_objects:
            if obj == 'budget_category':
                create_response = self.client.get(f"%s?budget_id={self.budget.pk}" %
                                                  reverse('budget_budget_category_create_urlpattern'))
                update_response = self.client.get(f"%s?budget_id={self.budget.pk}" %
                                                  reverse('budget_budget_category_update_urlpattern',
                                                          kwargs={'pk': self.budget_category.pk}))
                delete_response = self.client.get(f"%s?budget_id={self.budget.pk}" %
                                                  reverse('budget_budget_category_delete_urlpattern',
                                                          kwargs={'pk': self.budget_category.pk}))
                self.assertEqual(create_response.status_code, 200)
                self.assertEqual(update_response.status_code, 200)
                self.assertEqual(delete_response.status_code, 200)
            else:
                view_response = self.client.get(reverse(f"budget_{obj}_list_urlpattern"))
                create_response = self.client.get(reverse(f"budget_{obj}_create_urlpattern"))
                update_response = self.client.get(reverse(f"budget_{obj}_update_urlpattern", kwargs={'pk': 1}))
                delete_response = self.client.get(reverse(f"budget_{obj}_delete_urlpattern", kwargs={'pk': 1}))
                self.assertEqual(view_response.status_code, 200)
                self.assertEqual(create_response.status_code, 200)
                self.assertEqual(update_response.status_code, 200)
                self.assertEqual(delete_response.status_code, 200)

    def test_client(self):
        user = self.refresh_user('non-superuser')
        self.client.force_login(user)
        no_permission_objects = ['advisor', 'client', 'expense', 'income', 'budget', 'budget_category']
        for obj in no_permission_objects:
            if obj == 'budget_category':
                create_response = self.client.get(f"%s?budget_id={self.budget.pk}" %
                                                  reverse('budget_budget_category_create_urlpattern'))
                update_response = self.client.get(f"%s?budget_id={self.budget.pk}" %
                                                  reverse('budget_budget_category_update_urlpattern',
                                                          kwargs={'pk': self.budget_category.pk}))
                delete_response = self.client.get(f"%s?budget_id={self.budget.pk}" %
                                                  reverse('budget_budget_category_delete_urlpattern',
                                                          kwargs={'pk': self.budget_category.pk}))
                self.assertEqual(create_response.status_code, 403)
                self.assertEqual(update_response.status_code, 403)
                self.assertEqual(delete_response.status_code, 403)
            else:
                view_response = self.client.get(reverse(f"budget_{obj}_list_urlpattern"))
                create_response = self.client.get(reverse(f"budget_{obj}_create_urlpattern"))
                update_response = self.client.get(reverse(f"budget_{obj}_update_urlpattern", kwargs={'pk': 1}))
                delete_response = self.client.get(reverse(f"budget_{obj}_delete_urlpattern", kwargs={'pk': 1}))
                self.assertEqual(view_response.status_code, 403)
                self.assertEqual(create_response.status_code, 403)
                self.assertEqual(update_response.status_code, 403)
                self.assertEqual(delete_response.status_code, 403)
