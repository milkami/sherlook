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

    def form_valid(self, form):
       
        remember_me = form.cleaned_data['remember_me']  # get remember me data from cleaned_data of form
        if not remember_me:
            self.request.session.set_expiry(0)  # if remember me is 
            self.request.session.modified = True
        return super(LogInView, self).form_valid(form)