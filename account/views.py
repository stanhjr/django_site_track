from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import redirect

from django.views.generic import FormView, TemplateView, DetailView

from account.forms import AccountDetailsForm, AccountSocialNetworkForm, AccountChangePasswordForm
from site_track.models import MyUser


class AccountSettings(LoginRequiredMixin, FormView):
    template_name = 'account_settings.html'
    success_url = '/account/settings/'
    form_class = AccountDetailsForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_social'] = AccountSocialNetworkForm(request=self.request)
        context['form_change_password'] = AccountChangePasswordForm(request=self.request)
        return context

    def handle_no_permission(self):
        return redirect('login')

    def get_form_kwargs(self):
        kw = super(AccountSettings, self).get_form_kwargs()
        kw['request'] = self.request
        return kw

    def form_invalid(self, form):
        return redirect('account-settings')

    def form_valid(self, form):
        # self.request.user.set_value_from_form(self.request, form)
        return super().form_valid(form=form)

    def post(self, request, *args, **kwargs):
        action = self.request.POST['action']
        if action == 'social_form':
            account_social_form = AccountSocialNetworkForm(request.POST, request=self.request)
            if account_social_form.is_valid():
                self.request.user.set_value_from_form(self.request, account_social_form)
                self.request.user.save()
        elif action == 'detail_form':
            account_details_form = AccountDetailsForm(request.POST, request=self.request)
            if account_details_form.is_valid():
                self.request.user.set_value_from_form(self.request, account_details_form)
                self.request.user.save()
        elif action == 'change_password_form':
            change_password_form = AccountChangePasswordForm(request.POST, request=self.request)
            if change_password_form.is_valid():
                self.request.user.set_password(change_password_form.data.get("password1"))
                self.request.user.save()
        elif action == 'billing_information_form':
            billing_information_form = ''

        return super().post(request)


class UserProfile(LoginRequiredMixin, DetailView):
    model = MyUser
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super(UserProfile, self).get_context_data(**kwargs)
        if self.object == self.request.user:
            context['is_my_account'] = True
        else:
            context['is_my_account'] = False
        return context







