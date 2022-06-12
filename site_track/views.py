from django.contrib import auth
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django_site_track.settings import SESSION_COOKIE_AGE_ADMIN, SESSION_COOKIE_AGE

from site_track.forms import UserCreationForm, LoginForm, RestorePassword


def main(request):
    return HttpResponse("Hey! It's your main view!!")


class Register(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    # success_url = '/'
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('login')


class Login(LoginView):
    success_url = '/'
    form_class = LoginForm
    template_name = 'login.html'

    def form_valid(self, form):
        auth.login(self.request, form.get_user())
        if self.request.user.is_superuser:
            self.request.session.set_expiry(SESSION_COOKIE_AGE_ADMIN)
            return super().form_valid(form)
        else:
            self.request.session.set_expiry(SESSION_COOKIE_AGE)
            return super().form_valid(form)


class Logout(LoginRequiredMixin, LogoutView):
    next_page = '/'
    login_url = 'login/'


class RestorePassword(TemplateView):
    template_name = 'restore_password.html'
    extra_context = {'remember_password_form': RestorePassword}

