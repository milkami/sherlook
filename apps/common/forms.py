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

        widgets = {
            'email': forms.TextInput(attrs={'placeholder':'name@example.com'}),
        }



    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        del self.fields['password2']
        self.fields['password1'].help_text = None


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