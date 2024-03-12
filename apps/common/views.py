from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import *
from apps.accounts.models import *
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, View, ListView
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from apps.questions.models import *
from django.contrib.auth import logout
import math
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'commons/signup.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(reverse_lazy('login'))


class LogInView(LoginView):
    form_class = LogInForm
    success_url = '/search/'
    template_name = 'commons/login.html'

    def form_valid(self, form):
       
        remember_me = form.cleaned_data['remember_me']  # get remember me data from cleaned_data of form
        if not remember_me:
            self.request.session.set_expiry(0)  # if remember me is 
            self.request.session.modified = True
        if form.get_user():
            auth_login(self.request, form.get_user())
            return HttpResponseRedirect(self.success_url)
        else:
            return redirect('/login/')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)


def faq_view(request):
    if request.user.is_authenticated:
        questions = Questions.objects.filter(is_active=True).order_by('id')
        questions_half = math.ceil(questions.count()/2)
        questions_first = questions[0:questions_half]
        questions_second = questions[questions_half:questions.count()]
        return render(request, 'commons/faq.html', {'questions_first_half': questions_first, 'questions_second_half': questions_second})
    return redirect('/login/')


def profile_view(request):
    if request.user.is_authenticated:
        return render(request, 'commons/profile.html', {'user': request.user})
    return redirect('/login/')


def payment_view(request):
    if request.user.is_authenticated:
        user = CustomUser.objects.filter(email=request.user.email).first()
        orders = user.orders.filter(status='buy')
        subtotal = 0
        for order in orders:
            subtotal = subtotal + order.product.price
        return render(request, 'commons/payment.html', {'user': user, 'orders': orders, 'subtotal': subtotal})
    return redirect('/login/')


class SearchListView(ListView):
    model = Students
    template_name = 'commons/search.html'
    context_object_name = 'students'
    paginate_by = 45

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/')  # Replace 'login' with your actual login URL
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return Students.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        country = sorted(list(Students.objects.values_list('country', flat=True).distinct()))
        position = sorted(list(Students.objects.values_list('study', flat=True).distinct()))
        saved = self.request.user.orders.all().filter(status='saved').values_list('product', flat=True)
        specializations = sorted(list(Students.objects.values_list('specialisation', flat=True).distinct()))
        orders = self.request.user.orders.all()

        context['country'] = country
        context['position'] = position
        context['specializations'] = specializations
        context['saved'] = saved

        return context

    
def info_view(request):
    if request.user.is_authenticated:
        return render(request, 'commons/info.html')
    return redirect('/login/')


class LibraryListView(ListView):
    model = Students
    template_name = 'commons/library.html'
    context_object_name = 'students'
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/')  # Replace 'login' with your actual login URL
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        order = self.request.user.orders.all().values_list('product', flat=True)
        students = Students.objects.filter(id__in=order)
        return students

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        saved = self.request.user.orders.all().filter(status='saved').values_list('product', flat=True)
        connected = self.request.user.orders.all().filter(status='connected').values_list('product', flat=True)

        context['saved'] = saved
        context['connected'] = connected

        return context


def dashboard_view(request):
    if request.user.is_authenticated:
        return render(request, 'commons/dashboard.html')
    return redirect('/login/')


class UpdateOrderView(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request, student_id):
        data = {}
        if request.data['status']:
            if request.data['status'] != 'removed':
                student = Students.objects.get(id=student_id)
                order_obj, created = Order.objects.update_or_create(
                    customer=request.user,
                    product=student,
                    defaults={
                        "status": request.data['status'],

                    }
                )
                data['saved'] = self.request.user.orders.all().filter(status='saved').values_list('product', flat=True).count()
                data['connected'] = self.request.user.orders.all().filter(status='connected').values_list('product', flat=True).count()
                data['message'] = 'Student updated successfully'
            else:
                student = Students.objects.get(id=student_id)
                Order.objects.filter(customer=request.user, product=student).delete()
                data['saved'] = self.request.user.orders.all().filter(status='saved').values_list('product', flat=True).count()
                data['connected'] = self.request.user.orders.all().filter(status='connected').values_list('product', flat=True).count()
                data['message'] = 'Student updated successfully'
        else:
            data['message'] = 'Status field is missing'

        return JsonResponse(data)


def remove_from_library(request, pk):
    if request.user.is_authenticated:
        student = Students.objects.get(id=pk)
        Order.objects.filter(customer=request.user, product=student).delete()
        return redirect('/library')
    return redirect('/login/')


