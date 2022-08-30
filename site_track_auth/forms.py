from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm

from site_track.models import MyUser
from email_sender.tasks import generate_key, send_registration_link_to_email


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="email",
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
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            self.user = authenticate(username=username, password=password)

            if self.user is None:
                raise forms.ValidationError(message='username or password fields does not match')
            if self.user.is_confirm is False:
                raise forms.ValidationError(message='Please follow the instructions we just emailed for you!')

        return cleaned_data


class UserSignUpForm(forms.ModelForm):
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

    full_name = forms.CharField(label="full_name",
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

    company = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'enter company name'
        }
    ))
    position_in_company = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'enter position in company'
        }
    ))
    address_of_company = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'enter address in company'
        }
    ))
    number_of_trucks_in_fleet = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'enter number of trucks in fleet'
        }
    ))
    telephone_number_direct = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'enter telephone number direct'
        }
    ))
    phone_number = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'enter phone number'
        }
    ))

    class Meta:
        model = MyUser
        fields = ("full_name", "email", "company", "position_in_company",
                  "address_of_company", "number_of_trucks_in_fleet", "telephone_number_direct", "phone_number")

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

    def save(self, commit=True):
        user = super(UserSignUpForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.username = self.cleaned_data["email"]
        user.full_name = self.cleaned_data["full_name"]
        code = generate_key()
        user.code = code
        if commit:
            user.save()
            send_registration_link_to_email.delay(code=code, email_to=user.username)
        return user


class ResetPasswordForm(forms.Form):
    email = forms.CharField(label="email",
                            widget=forms.EmailInput(
                                attrs={
                                    'class': 'form-control',
                                    'placeholder': 'enter email address'
                                }
                            ))

    def clean(self):
        cleaned_data = super().clean()
        if MyUser.objects.filter(email=cleaned_data.get('email')).first():
            return cleaned_data
        #     self.fields.add_error('email', 'This mail is already registered')
        # return cleaned_data


class RestorePasswordForm(forms.Form):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(RestorePasswordForm, self).__init__(*args, **kwargs)

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

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('password_mismatch')
        return cleaned_data
