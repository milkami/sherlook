from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import *
from apps.accounts.models import *
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView, CreateView, View
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect, QueryDict
from django.shortcuts import redirect
from apps.questions.models import *
from django.core.mail import EmailMessage
from sherlook import settings
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from django.contrib import messages


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'commons/signup.html'


class LogInView(LoginView):
    form_class = LogInForm
    success_url = '/home/'
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


def faq_view(request):
    if request.user.is_authenticated:
        questions = Questions.objects.filter(is_active=True)
        return render(request, 'commons/faq.html', {'questions': questions})
    return render(request, 'commons/login.html', )


def profile_view(request):
    if request.user.is_authenticated:
        user = CustomUser.objects.filter(email=request.user.email).first()
        return render(request, 'commons/profile.html', {'user': user})
    return render(request, 'commons/login.html',)


def payment_view(request):
    if request.user.is_authenticated:
        user = CustomUser.objects.filter(email=request.user.email).first()
        orders = user.orders.filter(status='buy')
        subtotal = 0
        for order in orders:
            subtotal = subtotal + order.product.price
        return render(request, 'commons/profile.html', {'user': user, 'orders': orders, 'subtotal': subtotal})
    return render(request, 'commons/payment.html',)


class EmailAttachementView(View):
    form_class = EmailForm
    template_name = 'commons/support.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            form = self.form_class()
            return render(request, self.template_name, {'email_form': form})
        return render(request, 'commons/login.html', )


    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():

            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            # email = form.cleaned_data['email']
            files = request.FILES.getlist('attach')

            # if request.method == "POST":
            #     sender = request.POST.get('sender')
            #     toemail = request.POST.get('to')
            #     toname = request.POST.get('toname')
            #     fromemail = request.POST.get('from')
            #     subject = request.POST.get('subject')
            #     message = request.POST.get('message')
            # configuration = sib_api_v3_sdk.Configuration()
            # configuration.api_key['api-key'] = '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'
            # api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
            # subject = subject
            # html_content = message
            # sender = {"name": "Sherlook", "email": "mila.po@hotmail.com"}
            # to = [{"email": "milka.milicevic3@gmail.com", "name": "smece"}]
            # headers = {"Some-Custom-Name": "unique-id-1234"}
            # send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(attachment=files, to=to, headers=headers, html_content=html_content, sender=sender, subject=subject)
            # try:
            #     api_response = api_instance.send_transac_email(send_smtp_email)
            #
            #     messages.success(request, "Email send successfully")
            # except ApiException as e:
            #     print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)
            # return render(request, 'commons/support.html')



            try:
                mail = EmailMessage(subject, message, settings.EMAIL_HOST_USER, ['mila.po@hotmail.com'])
                for f in files:
                    mail.attach(f.name, f.read(), f.content_type)
                mail.send()
                return render(request, self.template_name,
                              {'email_form': form, 'error_message': 'Sent email to mila.po@hotmail.com', })
            except:
                return render(request, self.template_name,
                              {'email_form': form, 'error_message': 'Either the attachment is too big or corrupt'})

        return render(request, self.template_name,
                      {'email_form': form, 'error_message': 'Unable to send email. Please try again later'})