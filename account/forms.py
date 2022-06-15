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
            else:
                self.fields[field].widget = forms.TextInput(attrs={'class': 'form-control'})


class AccountSocialNetwork(forms.ModelForm):

    class Meta:
        model = MyUser
        fields = ('facebook', 'instagram', 'twitter', 'youtube', 'whatsapp', 'pinterest')
        # widgets = {}

    def __init__(self, user, *args, **kwargs):
        super(AccountSocialNetwork, self).__init__(user, *args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'




