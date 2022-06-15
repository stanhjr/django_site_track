from datetime import date
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Sum


class MyUser(AbstractUser):

    ACCOUNT_TYPE_CHOICES = (
        ("individual", "individual"),
        ("dealership", "dealership"),
    )

    money_spent = models.PositiveIntegerField(default=0)
    full_name = models.CharField(max_length=120, null=True)
    subscription = models.BooleanField(default=False)
    is_confirm = models.BooleanField(default=False)
    reset_password_code = models.CharField(max_length=120, null=True)
    code = models.CharField(max_length=120, null=True)
    account_name = models.CharField(max_length=60, null=True)
    account_type = models.CharField(max_length=120, null=True, choices=ACCOUNT_TYPE_CHOICES, default="individual")
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

    @property
    def get_photo_url(self):
        if self.profile_image:
            return self.profile_image.url
        else:
            return "/static/images/user.jpg"

    def set_value_from_form(self, request, form):
        image_link = self.profile_image
        for key, value in form.data.items():
            if key != "csrfmiddlewaretoken":
                setattr(self, key, value)
        if request.FILES.get('profile_image'):
            self.profile_image = request.FILES['profile_image']
        else:
            self.profile_image = image_link
        self.save()
        return self


class SaleAds(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='sale_ads')
    title = models.CharField(max_length=120, null=False)
    vehicle_registration_number = models.CharField(max_length=120)
    vehicle_registration_plate = models.CharField(max_length=120)
    date_of_issue = models.DateField()
    date_of_expire = models.DateField()
    vehicle_type = models.CharField(max_length=60)

    vehicle_make = models.CharField(max_length=60)
    vehicle_fuel = models.CharField(max_length=60)
    vehicle_colour = models.CharField(max_length=60)
    vehicle_millage = models.CharField(max_length=60)
    vehicle_price_amount = models.BigIntegerField(default=1000)
    vehicle_price_type = models.CharField(max_length=60)
    vehicle_condition = models.CharField(max_length=60)
    description = models.TextField(max_length=1500)

    @property
    def get_vehicle_features(self):
        if self.vehicle_features:
            return True

    @property
    def get_vehicle_photo_video(self):
        if self.vehicle_photo_video:
            return True
        return False


class VehicleFeatures(models.Model):
    sale_ads = models.OneToOneField(SaleAds, on_delete=models.CASCADE, related_name='vehicle_features')
    power_steering = models.BooleanField(default=False)
    trunk_light = models.BooleanField(default=False)
    sensing_lock = models.BooleanField(default=False)
    rain_sensing = models.BooleanField(default=False)
    vanity_mirror = models.BooleanField(default=False)
    bluetooth = models.BooleanField(default=False)
    cruise_control = models.BooleanField(default=False)
    alarm_system = models.BooleanField(default=False)
    cd_player = models.BooleanField(default=False)
    am_fm_radio = models.BooleanField(default=False)
    driver_air_bag = models.BooleanField(default=False)
    air_conditioning = models.BooleanField(default=False)
    panoramic_roof = models.BooleanField(default=False)
    integrated_phone = models.BooleanField(default=False)
    cylinders = models.BooleanField(default=False)


class VehiclePhotoVideo(models.Model):
    sale_ads = models.OneToOneField(SaleAds, on_delete=models.CASCADE, related_name='vehicle_photo_video')
    preview_image = models.ImageField(upload_to="images/")
    video_url = models.CharField(max_length=1024)
    facebook = models.CharField(max_length=60, null=True)
    instagram = models.CharField(max_length=60, null=True)
    twitter = models.CharField(max_length=60, null=True)
    youtube = models.CharField(max_length=60, null=True)
    whatsapp = models.CharField(max_length=60, null=True)
    pinterest = models.CharField(max_length=60, null=True)
















