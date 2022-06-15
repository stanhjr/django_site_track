from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import model_to_dict
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import FormView
from django.views.generic.edit import FormMixin

from account.forms import AccountDetailsForm
from site_track.models import MyUser


class AccountSettings(LoginRequiredMixin, FormView, FormMixin):
    template_name = 'account_settings.html'
    form_class = AccountDetailsForm
    success_url = '/account/settings/'

    def handle_no_permission(self):
        return redirect('login')

    def get_form_kwargs(self):
        kw = super(AccountSettings, self).get_form_kwargs()
        kw['request'] = self.request
        return kw

    def form_invalid(self, form):
        form.is_valid()
        return redirect('login')

    def form_valid(self, form):
        user = MyUser.objects.filter(email=self.request.user.email).first()
        for key in form.data:
            if key != "csrfmiddlewaretoken":
                setattr(user, key, form.data.get(key))
        user.profile_image = self.request.FILES['profile_image']
        return super().form_valid(form=form)





