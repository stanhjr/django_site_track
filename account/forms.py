from django import forms
from django.forms.models import model_to_dict
from site_track.models import MyUser


class AccountDetailsForm(forms.ModelForm):
    class Meta:
        model = MyUser

        fields = ('profile_image', 'account_name', 'account_type',
                  'phone_number', 'email', 'city',
                  'zip', 'about_vendor', 'state', 'web_site')

    def __init__(self, *args, **kwargs):
        self.ACCOUNT_TYPE_CHOICES = (
            ("individual", "individual"),
            ("dealership", "dealership"),
        )

        self.request = kwargs.pop('request', None)
        super(AccountDetailsForm, self).__init__(*args, **kwargs)
        self.user_dict = model_to_dict(self.request.user)
        for field in self.fields:
            self.fields[field].initial = self.user_dict.get(field)
            if field == "profile_image":
                self.fields[field].widget = forms.FileInput(attrs={'class': 'file-input', 'id': 'profile'})
            elif field == "account_type":
                self.fields[field].widget = forms.Select(attrs={'class': 'form-select'},
                                                         choices=self.ACCOUNT_TYPE_CHOICES)
            elif field == "about_vendor":
                self.fields[field].widget = forms.Textarea(attrs={'class': 'form-control'})
            else:
                self.fields[field].widget = forms.TextInput(attrs={'class': 'form-control'})


class AccountSocialNetworkForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ('facebook', 'instagram', 'twitter', 'youtube', 'whatsapp', 'pinterest')

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(AccountSocialNetworkForm, self).__init__(*args, **kwargs)
        self.user_dict = model_to_dict(self.request.user)
        for field in self.fields:
            self.fields[field].initial = self.user_dict.get(field)
            self.fields[field].widget = forms.TextInput(attrs={'class': 'form-control', 'type': 'url'})


class AccountChangePasswordForm(forms.Form):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(AccountChangePasswordForm, self).__init__(*args, **kwargs)

    password = forms.CharField(label="Password",
                               widget=forms.PasswordInput(
                                   attrs={
                                       'class': 'form-control',
                                   }
                               ))
    password1 = forms.CharField(label="Password",
                                widget=forms.PasswordInput(
                                    attrs={
                                        'class': 'form-control',
                                    }
                                ))
    password2 = forms.CharField(label="Password",
                                widget=forms.PasswordInput(
                                    attrs={
                                        'class': 'form-control',
                                    }
                                ))

    def clean_password(self):
        password = self.cleaned_data.get("password")
        if not self.request.user.check_password(password):
            raise forms.ValidationError('password_mismatch', code='password_mismatch',)
        return password

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('password_mismatch', code='password_mismatch', )
        return password2

