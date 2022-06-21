import datetime
from datetime import date
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Sum
from django.utils import timezone

from site_track.defoul_text_in_site import ABOUT_COMPANY_TEXT, ABOUT_COMPANY_TITLE


class MyUser(AbstractUser):

    ACCOUNT_TYPE_CHOICES = (
        ("individual", "individual"),
        ("dealership", "dealership"),
    )

    money_spent = models.PositiveIntegerField(default=0)
    full_name = models.CharField(max_length=120, null=True)
    subscription = models.BooleanField(default=False)
    subscribe_until_date = models.DateField(null=True)
    created_at = models.DateField(auto_now=True)
    is_confirm = models.BooleanField(default=False)
    reset_password_code = models.CharField(max_length=120, null=True)
    code = models.CharField(max_length=120, null=True)
    account_name = models.CharField(max_length=60, null=True)
    account_type = models.CharField(max_length=120, null=True, choices=ACCOUNT_TYPE_CHOICES, default="individual")
    phone_number = models.CharField(max_length=30, null=True)
    web_site = models.CharField(max_length=120, null=True)
    country = models.CharField(max_length=120, null=True)
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

    def add_subscription(self, days_number: int):
        if not self.subscribe_until_date:
            self.subscription = timezone.now() + timezone.timedelta(days=days_number)
        elif self.subscribe_until_date <= timezone.now():
            self.subscription = timezone.now() + timezone.timedelta(days=days_number)
        else:
            self.subscription += timezone.timedelta(days=days_number)

    @property
    def get_subscription(self):
        if self.subscribe_until_date <= timezone.now():
            return True
        return False

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

    @property
    def get_sale_ads_count(self):
        if self.sale_ads:
            return self.sale_ads.count()
        return 0


class CategoriesTrack(models.Model):
    image = models.ImageField(upload_to="category_images/", null=True)
    name = models.CharField(max_length=120)

    @classmethod
    def get_choices(cls):
        return [(tq.pk, tq.name) for tq in cls.objects.all()]

    @property
    def get_image_url(self):
        if self.image:
            return self.image.url
        else:
            return "/static/images/user.jpg"

    def __str__(self):
        return self.name


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
    # category = models.ForeignKey(CategoriesTrack, on_delete=models.SET_NULL, related_name='sale_ads')

    def __str__(self):
        return f"{self.title} by {self.user}"

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

    def __str__(self):
        return f"image in gallery for {self.gallery.title}"

    @property
    def get_image_url(self):
        if self.image:
            return self.image.url
        else:
            return "/static/images/user.jpg"


class SettingsFooter(models.Model):
    about_company_title = models.TextField(null=True, default=ABOUT_COMPANY_TITLE)
    about_company_text = models.TextField(null=True, default=ABOUT_COMPANY_TEXT)
    facebook_url = models.URLField(null=True, default="https://www.facebook.com/")
    twitter_url = models.URLField(null=True, default="https://twitter.com/")
    linkedin_url = models.URLField(null=True, default="https://www.linkedin.com/")
    whatsapp_phone = models.CharField(null=True, max_length=60, default="")
    youtube_url = models.URLField(null=True, default="https://www.youtube.com/")
    email_1 = models.EmailField(null=True, default="info@example.com")
    email_2 = models.EmailField(null=True, default="carrer@example.com")
    phone_number_1 = models.CharField(null=True, max_length=120, default="+91 987-654-3210")
    phone_number_2 = models.CharField(null=True, max_length=120, default="+91 987-654-5466")
    address_top = models.CharField(null=True, max_length=120, default="1Hd- 50, 010 Avenue")
    address_bottom = models.CharField(null=True, max_length=120, default="NY 90001 United States")
    news_letter_title = models.CharField(null=True, max_length=120, default="Our Newsletter")
    news_letter_text = models.CharField(null=True, max_length=300, default="Be the first to know about our offers and discounts by subscribing to the newsletter")


class SettingsHeaderHome(models.Model):
    header_title = models.CharField(null=True, max_length=120, default="Used Equipment or Sale")
    header_text = models.CharField(null=True, max_length=500, default="Browse through thousands of affordable alternatives to new equipment. View our detailed inspection reports and buy with confidence")
    contact_email = models.EmailField(null=True, default="info@example.com")
    contact_number = models.CharField(null=True, max_length=120, default="+91 987-654-3210")


class SettingsIndexHome(models.Model):
    find_top_categories_title = models.TextField(default="find top categories")
    find_top_categories_text = models.TextField(default="Lorem ipsum dolor sit amet consectetur adipisicing")
    our_features_listing_title = models.TextField(default="our featured listing")
    our_features_listing_text = models.TextField(default="Lorem ipsum dolor sit amet consectetur adipisicin")
    brand_part_title = models.TextField(default="browse by top brands")
    brand_part_text = models.TextField(default="Lorem ipsum dolor sit amet consectetur adipisicin")
    price_part_title = models.TextField(default="our ads pricing plans")
    price_part_text = models.TextField(default="Lorem ipsum dolor sit amet consectetur adipisicin")
    # review_part_title = models.TextField(default="Lorem ipsum dolor sit amet consectetur adipisicin")
    # review_part_title = models.TextField(default="Lorem ipsum dolor sit amet consectetur adipisicin")
    recent_part_title = models.TextField(default="recent add vehiclesn")
    reent_part_text = models.TextField(default="Lorem ipsum dolor sit amet consectetur adipisicin")


if not SettingsFooter.objects.last():
    SettingsFooter.objects.create()


if not CategoriesTrack.objects.last():
    CategoriesTrack.objects.create(name="Minivan", image="category_images/minivan.png")
    CategoriesTrack.objects.create(name="Convertible", image="category_images/convertible.png")
    CategoriesTrack.objects.create(name="Coupe", image="/category_images/coupe.png")
    CategoriesTrack.objects.create(name="Hatchback", image="/category_images/hatchback.png")
    CategoriesTrack.objects.create(name="Jeep", image="/category_images/jeep.png")
    CategoriesTrack.objects.create(name="Pickup", image="/category_images/pickup.png")
    CategoriesTrack.objects.create(name="Suv", image="/category_images/suv.png")
    CategoriesTrack.objects.create(name="Sedan", image="/category_images/sedan.png")
    CategoriesTrack.objects.create(name="Wagon", image="/category_images/wagon.png")
    CategoriesTrack.objects.create(name="Sports", image="/category_images/sports.png")














