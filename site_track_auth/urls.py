"""django_site_track URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from site_track_auth.views import Login, Logout, SignUp, RestorePassword, SignUpConfirm, FollowEmail, ResetPassword, \
    ResetPasswordConfirm

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('logout/', Logout.as_view(), name='logout'),
    path('restore-password/',  RestorePassword.as_view(), name='restore-password'),
    path('account-activate/', SignUpConfirm.as_view(), name='account-activate'),
    path('follow-email/', FollowEmail.as_view(), name='follow-email'),
    path('reset-password/', ResetPassword.as_view(), name='reset-password'),
    path('reset-password-confirm/', ResetPasswordConfirm.as_view(), name='reset-password-confirm'),
]
