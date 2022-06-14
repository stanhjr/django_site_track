from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm


from site_track.models import MyUser
from site_track.tools.send_email import generate_key, send_registration_link_to_email

