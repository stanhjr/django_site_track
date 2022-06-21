import random

from django.contrib import auth
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, UpdateView, ListView
from site_track.forms import ContactForm

from site_track.models import MyUser, SaleAds, SettingsFooter
from site_track_auth.tools.send_email import send_main_contact_us


def main(request):
    return HttpResponse("Hey! It's your main view!!")


class ContactView(LoginRequiredMixin, FormView):
    template_name = 'contact.html'
    success_url = '/'
    form_class = ContactForm

    def handle_no_permission(self):
        return redirect('login')

    # def get_form_kwargs(self):
    #     kw = super(ContactView, self).get_form_kwargs()
    #     kw['request'] = self.request
    #     return kw

    def form_valid(self, form):
        send_main_contact_us(email_from=form.data.get("email"),
                             subject=form.data.get("subject"),
                             text=form.data.get("text"))
        return super().form_valid(form=form)


class IndexView(ListView):
    model = SaleAds
    template_name = 'index.html'
    paginate_by = 16

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return super().get_queryset().order_by('-vehicle_price_amount')[:4]
        return super().get_queryset()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['recent_objects'] = SaleAds.objects.order_by('-created_at')[:4]
        context['footer'] = SettingsFooter.objects.last()
        return context



