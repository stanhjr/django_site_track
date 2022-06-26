from django.contrib import auth
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, RedirectView, FormView
from django_site_track.settings import SESSION_COOKIE_AGE_ADMIN, SESSION_COOKIE_AGE

from site_track_auth.forms import UserSignUpForm, LoginForm, ResetPasswordForm, RestorePasswordForm
from site_track.models import MyUser, SettingsFooter, SettingsAuthBase
from email_sender.tasks import generate_key, send_reset_password_link_to_email


class SignUp(CreateView):
    form_class = UserSignUpForm
    template_name = 'auth/sign_up.html'
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('follow-email')

    def get_context_data(self, **kwargs):
        context = super(SignUp, self).get_context_data(**kwargs)
        context['social_link'] = SettingsFooter.objects.last()
        context['auth_base'] = SettingsAuthBase.objects.last()
        context['title'] = 'sign up'
        return context


class Login(LoginView):
    success_url = 'account/settings'
    form_class = LoginForm
    template_name = 'auth/login.html'

    def form_valid(self, form):
        auth.login(self.request, form.get_user())
        if self.request.user.is_superuser:
            self.request.session.set_expiry(SESSION_COOKIE_AGE_ADMIN)
        else:
            self.request.session.set_expiry(SESSION_COOKIE_AGE)
        return redirect('account-settings')

    def get_context_data(self, **kwargs):
        context = super(Login, self).get_context_data(**kwargs)
        context['social_link'] = SettingsFooter.objects.last()
        context['auth_base'] = SettingsAuthBase.objects.last()
        context['title'] = 'login'
        return context


class Logout(LoginRequiredMixin, LogoutView):
    next_page = reverse_lazy('login')
    login_url = 'login/'


class FollowEmail(TemplateView):
    template_name = 'auth/follow_email.html'


class ResetPasswordConfirm(TemplateView):
    template_name = 'auth/reset_password_confirm.html'


class SignUpConfirm(RedirectView):

    def dispatch(self, request, *args, **kwargs):
        code = self.request.GET.get("code")
        user = MyUser.objects.filter(code=code).first()
        if user:
            user.code = ''
            user.is_confirm = True
            user.save()
            return redirect('login')
        else:
            return redirect('sign-up')


class ResetPassword(FormView):
    template_name = 'auth/reset_password.html'
    form_class = ResetPasswordForm
    success_url = '/'

    def form_valid(self, form):
        user = MyUser.objects.filter(email=form.data.get('email'), is_confirm=True).first()
        if user:
            user.is_reset_password = True
            user.reset_password_code = generate_key()
            send_reset_password_link_to_email.delay(user.reset_password_code, user.email)
            user.save()
            return redirect('reset-password-confirm')

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ResetPassword, self).get_context_data(**kwargs)
        context['social_link'] = SettingsFooter.objects.last()
        context['auth_base'] = SettingsAuthBase.objects.last()
        context['title'] = 'reset password'
        return context


class RestorePassword(FormView):
    success_url = '/'
    form_class = RestorePasswordForm
    template_name = 'auth/restore_password.html'

    def get_form_kwargs(self):
        kw = super(RestorePassword, self).get_form_kwargs()
        kw['request'] = self.request
        return kw

    def form_valid(self, form):
        user = MyUser.objects.filter(reset_password_code=self.request.GET.get("code")).first()
        if user:
            user.reset_password_code = ''
            user.set_password(form.data.get('password1'))
            user.save()
            return redirect('login')
        return redirect('sign-up')

