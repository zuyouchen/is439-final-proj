from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from django.views.generic import TemplateView, RedirectView

urlpatterns = [
    path('',
         RedirectView.as_view(
             pattern_name='home_urlpattern',
             permanent=False
         )),

    path('home/',
         TemplateView.as_view(template_name='budget/home.html'),
         name='home_urlpattern'),

    path('about/',
         TemplateView.as_view(template_name='budget/about.html'),
         name='about_urlpattern'),

    path('login/',
         LoginView.as_view(template_name='budget/login.html'),
         name='login_urlpattern'),

    path('logout/',
         LogoutView.as_view(),
         name='logout_urlpattern'),

    path('admin/', admin.site.urls),

    path('', include('budget.urls'))
]
