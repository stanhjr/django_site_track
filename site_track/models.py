from datetime import date
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Sum


class MyUser(AbstractUser):
    money_spent = models.PositiveIntegerField(default=0)
    subscription = models.BooleanField(default=False)






