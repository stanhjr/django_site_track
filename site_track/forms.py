from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm

from site_track.models import MyUser


class RestorePassword(forms.Form):
    email = forms.CharField(label="email",
                            widget=forms.EmailInput(
                                attrs={
                                    'class': 'form-control',
                                    'placeholder': 'enter email address'
                                }
                            ))


class LoginForm(AuthenticationForm):
    email = forms.CharField(label="email",
                            widget=forms.EmailInput(
                                attrs={
                                    'class': 'form-control',
                                    'placeholder': 'enter email address'
                                }
                            ))
    password = forms.CharField(label="Password confirmation",
                               widget=forms.PasswordInput(
                                   attrs={
                                       'class': 'form-control',
                                       'placeholder': 'enter repeat password'
                                   }
                               ))

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            self.user = authenticate(email=email, password=password)
            if self.user is None:
                raise forms.ValidationError(message='username or password fields does not match')


class UserCreationForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """

    error_messages = {
        'password_mismatch': "The two password fields didn't match.",
    }
    password1 = forms.CharField(label="Password",
                                widget=forms.PasswordInput(
                                    attrs={
                                        'class': 'form-control',
                                        'placeholder': 'enter strong password'
                                    }
                                ))
    password2 = forms.CharField(label="Password confirmation",
                                widget=forms.PasswordInput(
                                    attrs={
                                        'class': 'form-control',
                                        'placeholder': 'enter repeat password'
                                    }
                                ))

    username = forms.CharField(label="username",
                               max_length=50,
                               widget=forms.TextInput(
                                   attrs={
                                       'class': 'form-control',
                                       'placeholder': 'enter full name'
                                   }
                               ))

    email = forms.CharField(label="email", widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'enter email address'
        }
    ))

    class Meta:
        model = MyUser
        fields = ("username", "email")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def clean(self):
        cleaned_data = super().clean()
        if MyUser.objects.filter(email=cleaned_data.get('email')).exists():
            self.fields.add_error('email', 'This mail is already registered')
        return cleaned_data
