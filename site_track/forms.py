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

    def clean(self):
        cleaned_data = super().clean()
        print(cleaned_data)
        print(cleaned_data["email"])
        print(cleaned_data["account_name"])
        print(cleaned_data["account_type"])
        print(cleaned_data["city"])
        print(cleaned_data["zip"])
        print(cleaned_data["state"])
        print(cleaned_data["phone_number"])
        print(cleaned_data["about_vendor"])
        print(cleaned_data["web_site"])
        return cleaned_data

    # def save(self, commit=True):
    #
    #     user = MyUser.objects.filter(email=self.request.user.email)
    #     print('=====================================')
    #     print(434343434)
    #     print('=====================================')
    #     user.email = self.cleaned_data["email"]
    #     user.account_name = self.cleaned_data["account_name"]
    #     user.account_type = self.cleaned_data["account_type"]
    #     user.city = self.cleaned_data["city"]
    #     user.zip = self.cleaned_data["zip"]
    #     user.state = self.cleaned_data["state"]
    #     user.profile_image = self.cleaned_data["image"]
    #     user.phone_number = self.cleaned_data["phone_number"]
    #     user.about_vendor = self.cleaned_data["about_vendor"]
    #     user.save()
    #     if commit:
    #         user.save()
    #     return user
