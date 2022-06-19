import datetime
from datetime import date
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Sum
from django.utils import timezone


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

    @property
    def get_sale_created(self):
        return self.sale_ads.filter(sale_created=True).first()

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
    sale_created = models.BooleanField(default=True)

    power_steering = models.BooleanField(default=False)
    trunk_light = models.BooleanField(default=False)
    sensing_lock = models.BooleanField(default=False)
    rain_sensing = models.BooleanField(default=False)
    vanity_mirror = models.BooleanField(default=False)
    bluetooth = models.BooleanField(default=False)
    cruise_control = models.BooleanField(default=False)
    alarm_system = models.BooleanField(default=False)
    cylinders = models.BooleanField(default=False)
    cd_player = models.BooleanField(default=False)
    am_fm_radio = models.BooleanField(default=False)
    driver_air_bag = models.BooleanField(default=False)
    air_conditioning = models.BooleanField(default=False)
    panoramic_roof = models.BooleanField(default=False)
    integrated_phone = models.BooleanField(default=False)
    title = models.CharField(max_length=120, null=True)
    vehicle_registration_number = models.CharField(max_length=120, null=True)
    vehicle_registration_plate = models.CharField(max_length=120, null=True)
    date_of_issue = models.DateField(null=True)
    date_of_expire = models.DateField(null=True)
    vehicle_year = models.DateField(null=True)
    vehicle_type = models.CharField(max_length=60, null=True)
    vehicle_make = models.CharField(max_length=60, null=True)
    vehicle_fuel = models.CharField(max_length=60, null=True)
    vehicle_colour = models.CharField(max_length=60, null=True)
    vehicle_mileage = models.BigIntegerField(default=10000, null=True)
    vehicle_transmission = models.CharField(max_length=60, default="Manual")
    vehicle_price_amount = models.BigIntegerField(default=1000, null=True)
    vehicle_price_type = models.CharField(max_length=60, null=True)
    vehicle_wheel = models.CharField(max_length=60, default="Left")
    vehicle_wheel_drive = models.CharField(max_length=60, default="Rear-Drive")
    vehicle_condition = models.CharField(max_length=60, null=True)
    description = models.TextField(max_length=1500, null=True)
    preview_image = models.ImageField(upload_to="images/", null=True)
    video_url = models.CharField(max_length=1024, null=True)
    facebook = models.CharField(max_length=120, null=True)
    instagram = models.CharField(max_length=120, null=True)
    twitter = models.CharField(max_length=120, null=True)
    youtube = models.CharField(max_length=120, null=True)
    pinterest = models.CharField(max_length=120, null=True)
    linkedin = models.CharField(max_length=120, null=True)
    country = models.CharField(max_length=120, null=True)
    city = models.CharField(max_length=120, null=True)
    state = models.CharField(max_length=120, null=True)
    post_code = models.CharField(max_length=120, null=True)
    ward_no = models.CharField(max_length=120, null=True)
    road_no = models.CharField(max_length=120, null=True)
    shop_no = models.CharField(max_length=120, null=True)
    phone_number = models.CharField(max_length=30, null=True)
    web_site = models.CharField(max_length=120, null=True)
    email = models.EmailField(max_length=120, null=True)
    others = models.TextField(max_length=500, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='sale_ads')

    def set_value_from_form(self, request, form):
        image_link = self.preview_image
        for key, value in form.data.items():
            if key != "csrfmiddlewaretoken":
                setattr(self, key, value)
        if request.FILES.get('preview_image'):
            self.profile_image = request.FILES['preview_image']
        else:
            self.profile_image = image_link
        self.save()
        return self

    @property
    def get_photo_url(self):
        if self.preview_image:
            return self.preview_image.url
        else:
            return "/static/images/user.jpg"

    @property
    def get_photo_in_gallery_count(self):
        if self.image_in_gallery:
            return self.image_in_gallery.count()
        return 0

    @property
    def get_date_ago(self):
        time = datetime.datetime.now()
        if self.created_at.day == time.day:
            return str(time.hour - self.created_at.hour) + " hours ago"
        else:
            if self.created_at.month == time.month:
                return str(time.day - self.created_at.day) + " days ago"
            else:
                if self.created_at.year == time.year:
                    return str(time.month - self.created_at.month) + " months ago"
        return self.created_at


class ImageInGallery(models.Model):
    gallery = models.ForeignKey(SaleAds, on_delete=models.CASCADE, related_name='image_in_gallery')
    image = models.ImageField(upload_to="images/")


















