from datetime import date
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Sum


class MyUser(AbstractUser):
    money_spent = models.PositiveIntegerField(default=0)
    full_name = models.CharField(max_length=120, null=True)
    subscription = models.BooleanField(default=False)
    is_confirm = models.BooleanField(default=False)
    reset_password_code = models.CharField(max_length=120, null=True)
    code = models.CharField(max_length=120, null=True)

    account_name = models.CharField(max_length=60, null=True)
    account_type = models.CharField(max_length=120, null=True)
    phone_number = models.CharField(max_length=30, null=True)
    web_site = models.CharField(max_length=120, null=True)
    city = models.CharField(max_length=60, null=True)
    state = models.CharField(max_length=60, null=True)
    zip = models.CharField(max_length=60, null=True)
    about_vendor = models.TextField(null=True)
    profile_image = models.ImageField(null=True, upload_to="images/")
    facebook = models.CharField(max_length=60, null=True)
    instagram = models.CharField(max_length=60, null=True)
    twitter = models.CharField(max_length=60, null=True)
    youtube = models.CharField(max_length=60, null=True)
    whatsapp = models.CharField(max_length=60, null=True)
    pinterest = models.CharField(max_length=60, null=True)












