from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView

from site_track.forms import AuthenticationForm, UserCreationForm


def main(request):
    return HttpResponse("Hey! It's your main view!!")


class Register(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = '/'


class Login(LoginView):
    success_url = '/'
    form_class = AuthenticationForm
    template_name = 'login.html'


class Logout(LoginRequiredMixin, LogoutView):
    next_page = '/'
    login_url = 'login/'
