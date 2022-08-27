# import datetime
# from django.contrib.auth.models import AbstractUser
# from django.core.validators import MinValueValidator, MaxValueValidator
# from django.db import models
# from django.utils import timezone
#
# from site_track.models import MyUser, SaleAds
#
#
# class Auction(models.Model):
#     last_price = models.PositiveIntegerField(default=0, null=True)
#     user_bet = models.OneToOneField(MyUser, on_delete=models.SET_NULL, related_name='auction_bet')
#     user_watch = models.ForeignKey(MyUser, on_delete=models.SET_NULL, related_name='auction_watch')
#     sale_ads = models.OneToOneField(SaleAds, on_delete=models.CASCADE, related_name='auction')
#     sale_end_time = models.DateTimeField()
#
#     def check_payment(self):
#         if self.last_price > self.sale_ads.vehicle_price_amount:
#             return True
#         return False
#
#     def save(self, *args, **kwargs):
#         ...
#         # TODO email notification celery
#
#         super(Auction, self).save(*args, **kwargs)
#
#     def send_notification(self):
#         if self.user_bet:
#             ...
#         # TODO email notification celery
#
#     def auction_ended(self):
#         # TODO send owner notification
#         if self.sale_ads.sales:
#             return True
#         if timezone.now() >= self.sale_end_time:
#             return True
#
#
#
#
#
#
