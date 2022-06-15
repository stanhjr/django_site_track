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

