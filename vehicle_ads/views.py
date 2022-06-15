from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy

from django.views.generic import FormView

from vehicle_ads.forms import VehicleInformationForm


class VehicleInformationView(LoginRequiredMixin, FormView):
    template_name = 'create-ads.html'
    success_url = reverse_lazy('create-ads')
    form_class = VehicleInformationForm

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['form_social'] = AccountSocialNetworkForm(request=self.request)
    #     context['form_change_password'] = AccountChangePasswordForm(request=self.request)
    #     return context

    def handle_no_permission(self):
        return redirect('login')

    def get_form_kwargs(self):
        kw = super(VehicleInformationView, self).get_form_kwargs()
        kw['request'] = self.request
        return kw

    def form_invalid(self, form):
        form.is_valid()
        return redirect('account-settings')

    def post(self, request, *args, **kwargs):
        action = self.request.POST['action']
        if action == 'vehicle-information':
            account_social_form = VehicleInformationForm(request.POST, request=self.request)
            if account_social_form.is_valid():
                self.request.user.sale_ads.set_value_from_form(self.request, account_social_form)
                self.request.user.sale_ads.save()

        return super().post(request)