from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import SignUpForm, LogInForm
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView, CreateView


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'commons/signup.html'


class LogInView(LoginView):
    form_class = LogInForm
    success_url = reverse_lazy('home')
    template_name = 'commons/login.html'