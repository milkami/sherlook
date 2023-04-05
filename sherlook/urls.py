"""
URL configuration for sherlook project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from apps.common.views import SignUpView, LogInView, TemplateView, EmailAttachementView
from django.contrib.auth import views as auth_views
from apps.common import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='example.html'), name='signup'),
    path('home/', TemplateView.as_view(template_name='commons/home.html'), name='home'),
    path('register/', SignUpView.as_view(), name="register"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', LogInView.as_view(), name='login'),
    path('faq/', views.faq_view, name='faq'),
    path('support/', EmailAttachementView.as_view(), name='support'),
    path('profile/', views.profile_view, name='profile'),
    path('payment/', views.payment_view, name='payment'),

]
