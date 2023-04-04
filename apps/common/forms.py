from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class SignUpForm(UserCreationForm):
    """
    A Custom form for creating new users.
    """

    class Meta:
        model = get_user_model()
        fields = [
            'first_name',
            'last_name',
            'email',
            'password1',
            'company_name',
            'number_of_employer',
        ]

        labels = {
            'email': 'E-mail'
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'First Name', 'style': 'margin-bottom: 10px',}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Last Name', 'style': 'margin-bottom: 10px',}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'name@example.com', 'style': 'margin-bottom: 10px',}),
            # 'password1': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'XXXXXXX'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Company Name', 'style': 'margin-bottom: 10px',}),
            'number_of_employer': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'', 'style': 'margin-bottom: 23px',}),
        }



    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        del self.fields['password2']
        self.fields['password1'].help_text = None
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder':'XXXXXXX', 'style': 'margin-bottom: 10px', 'autocomplete': 'off'})


class LogInForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False)
    """
    A Custom form for creating new users.
    """

    class Meta:
        model = get_user_model()
        fields = [
            'email',
            'password1',
        ]


    def __init__(self, *args, **kwargs):
        super(LogInForm, self).__init__(*args, **kwargs)
        # del self.fields['password2']
        self.fields['password'].required = False
        self.fields['username'].required = False
        self.fields['username'].label = 'E-mail'
        self.fields['username'].widget.attrs['placeholder'] = 'name@example.com'
        self.fields['password'].widget.attrs['placeholder'] = 'XXXXXXX'
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'style': 'margin-bottom: 10px', 'autocomplete': 'off'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'style': 'margin-bottom: 23px', 'autocomplete': 'off'})

class EmailForm(forms.Form):
    # email = forms.EmailField()
    subject = forms.CharField(max_length=100)
    attach = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)
    message = forms.CharField(widget=forms.Textarea)