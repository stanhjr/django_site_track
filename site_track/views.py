from django.contrib import auth
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, RedirectView, FormView, UpdateView
from django_site_track.settings import SESSION_COOKIE_AGE_ADMIN, SESSION_COOKIE_AGE
from site_track.forms import AccountDetailsForm

from site_track.models import MyUser


def main(request):
    return HttpResponse("Hey! It's your main view!!")


class AccountSettings(LoginRequiredMixin, FormView):
    template_name = 'account_settings.html'
    form_class = AccountDetailsForm
    success_url = '/settings'

    def get_initial(self):
        initial = super().get_initial()
        initial['image'] = self.request.user.profile_image
        initial['email'] = self.request.user.email
        initial['account_name'] = self.request.user.account_name
        initial['account_type'] = self.request.user.account_type
        initial['phone_number'] = self.request.user.phone_number
        initial['web_site'] = self.request.user.web_site
        initial['city'] = self.request.user.city
        initial['state'] = self.request.user.state
        initial['zip'] = self.request.user.zip
        initial['about_vendor'] = self.request.user.about_vendor

        return initial

    def get_form_kwargs(self):
        kw = super(AccountSettings, self).get_form_kwargs()
        kw['request'] = self.request
        return kw

    def handle_no_permission(self):
        return redirect('login')

    def form_invalid(self, form):
        form.is_valid()
        return redirect('login')

    def form_valid(self, form):
        user = MyUser.objects.filter(email=self.request.user.email).first()
        user.profile_image = self.request.FILES['image']
        user.web_site = form.data.get('web_site')
        user.email = form.data.get('email')
        user.account_name = form.data.get('account_name')
        user.account_type = form.data.get('account_type')
        user.city = form.data.get('city')
        user.zip = form.data.get('zip')
        user.state = form.data.get('state')
        user.phone_number = form.data.get('phone_number')
        user.about_vendor = form.data.get('about_vendor')
        user.save()
        return super().form_valid(form=form)
