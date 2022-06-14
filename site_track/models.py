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






