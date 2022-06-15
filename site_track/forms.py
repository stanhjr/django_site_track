from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm

from site_track.models import MyUser
from site_track.tools.send_email import generate_key, send_registration_link_to_email


class AccountDetailsForm(forms.Form):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(AccountDetailsForm, self).__init__(*args, **kwargs)

    class Meta:
        model = MyUser
        fields = ['profile_image', ]

    image = forms.ImageField(required=False,
                             widget=forms.FileInput(
                                 attrs={
                                     'class': 'file-input',
                                     'id': 'profile',
                                 }
                             ))

    account_name = forms.CharField(
        max_length=60,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        ))

    ACCOUNT_TYPE_CHOICES = (
        ("1", "individual"),
        ("2", "dealership"),
    )
    account_type = forms.ChoiceField(
        choices=ACCOUNT_TYPE_CHOICES,
        widget=forms.Select(
            attrs={
                'class': 'form-select'
            }
        ))
    phone_number = forms.CharField(
        max_length=60,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        ))
    email = forms.CharField(
        label="email",
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
            }
        ))
    web_site = forms.CharField(
        max_length=120,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        ))
    city = forms.CharField(
        max_length=60,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        ))
    state = forms.CharField(
        max_length=60,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        ))
    zip = forms.CharField(
        max_length=60,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        ))
    about_vendor = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control'
        }))
