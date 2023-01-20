from django.db import models


class Faq(models.Model):
    title = models.CharField(max_length=1000)
    text = models.TextField(max_length=10000)
    number = models.ImageField(default=1)

    def __str__(self):
        return self.title


class DateSubscribe(models.Model):
    date = models.DateField(null=True)

    def __str__(self):
        return f'subscription start date'


