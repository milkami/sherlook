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
from apps.common.views import SignUpView, LogInView, TemplateView, EmailAttachementView, LogoutView, SearchListView, UpdateOrderView, LibraryListView, remove_from_library
from django.contrib.auth import views as auth_views
from apps.common import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', LogInView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name="register"),
    path('faq/', views.faq_view, name='faq'),
    path('support/', EmailAttachementView.as_view(), name='support'),
    path('profile/', views.profile_view, name='profile'),
    path('payment/', views.payment_view, name='payment'),
    path('search/', SearchListView.as_view(), name='search'),
    path('info/', views.info_view, name='info'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('library/', LibraryListView.as_view(), name='library'),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('update_order/<int:student_id>/', UpdateOrderView.as_view(), name="update_order"),
    path('remove/<int:pk>/', remove_from_library, name='remove_from_library'),

]
