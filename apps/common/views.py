from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import *
from apps.accounts.models import *
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, View, ListView, TemplateView
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
from django.db.models import Q, F


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

    def save_query_params(self, params):
        self.request.session['search_params'] = params

    def get_query_params(self, position, specialization, country):
        q_objects = Q()
        if not position and not specialization and not country:
            return q_objects
        position = None if position == 'Any' else position
        specialization = None if specialization == 'Any' else specialization
        country = None if country == 'Any' else country
        if position:
            q_objects &= Q(position=position)
        if specialization:
            q_objects &= Q(specialisation=specialization)
        if country:
            q_objects &= Q(country=country)

        return q_objects

    def get_queryset(self):
        position = self.request.GET.get('position', default=None)
        specialization = self.request.GET.get('specialization', default=None)
        country = self.request.GET.get('country', default=None)
        experience = self.request.GET.get('experience', default=None)
        parms = self.get_query_params(position, specialization, country)

        # Retrieve saved query parameters from the session
        saved_params = self.retrieve_saved_query_params()
        if len(self.request.GET) < 1 and saved_params:
            position = saved_params.get('position')
            specialization = saved_params.get('specialization')
            country = saved_params.get('country')
            parms = self.get_query_params(position, specialization, country)
        else:
            self.save_query_params(self.request.GET.dict())
        if experience:
            students = Students.objects.filter(parms).extra(
                order_by=[F('experience').desc(nulls_last=True)]
            )
        else:
            students = Students.objects.filter(parms)
        return students

    def retrieve_saved_query_params(self):
        saved_params = self.request.session.get('search_params', {})

        return saved_params

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        country = sorted(list(Students.objects.values_list('country', flat=True).distinct()))
        position = sorted(list(Students.objects.values_list('study', flat=True).distinct()))
        saved = self.request.user.orders.all().filter(status='saved').values_list('product', flat=True)
        specializations = sorted(list(Students.objects.values_list('specialisation', flat=True).distinct()))
        is_first = False
        saved_params = self.retrieve_saved_query_params()
        if len(self.request.GET) < 1 and not saved_params:
            is_first = True

        context['country'] = ["Any"] + country
        context['position'] = ["Any"] + position
        context['specializations'] = ["Any"] + specializations
        context['saved'] = saved
        context['is_first'] = is_first

        return context

    
def info_view(request):
    if request.user.is_authenticated:
        library = request.GET.get('library', default=None)
        if library:
            return render(request, 'commons/info.html', {'library': "True"})
        else:
            return render(request, 'commons/info.html', {'library': "False"})
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


