from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import SignUpForm, LogInForm
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView, CreateView
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect, QueryDict
from django.shortcuts import redirect


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
        if form.get_user():
            auth_login(self.request, form.get_user())
            return HttpResponseRedirect(self.get_success_url())
        else:
            return redirect('/login/')