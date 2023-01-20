import datetime

import django
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone

from djstripe.models import Customer

from site_track.defoul_text_in_site import ABOUT_COMPANY_TEXT, ABOUT_COMPANY_TITLE


class MyUser(AbstractUser):
    ACCOUNT_TYPE_CHOICES = (
        ("individual", "individual"),
        ("dealership", "dealership"),
    )

    money_spent = models.PositiveIntegerField(default=0)
    company = models.CharField(max_length=120, null=True, blank=True)
    position_in_company = models.CharField(max_length=120, null=True, blank=True)
    address_of_company = models.CharField(max_length=120, null=True, blank=True)
    number_of_trucks_in_fleet = models.IntegerField(null=True)
    telephone_number_direct = models.CharField(max_length=30, null=True)

    subscription_one_time = models.BooleanField(default=False)
    subscribe_until_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    is_confirm = models.BooleanField(default=False)
    reset_password_code = models.CharField(max_length=120, null=True, blank=True)
    code = models.CharField(max_length=120, null=True, blank=True)
    account_name = models.CharField(max_length=60, null=True, blank=True)
    account_type = models.CharField(max_length=120, null=True, choices=ACCOUNT_TYPE_CHOICES, default="individual")
    phone_number = models.CharField(max_length=30, null=True)
    web_site = models.CharField(max_length=120, null=True, blank=True)
    country = models.CharField(max_length=120, null=True, blank=True)
    city = models.CharField(max_length=60, null=True, blank=True)
    state = models.CharField(max_length=60, null=True, blank=True)
    zip = models.CharField(max_length=60, null=True, blank=True)
    about_vendor = models.TextField(null=True, blank=True)
    profile_image = models.ImageField(null=True, upload_to="images/", blank=True)

    facebook = models.CharField(max_length=60, null=True, blank=True)
    instagram = models.CharField(max_length=60, null=True, blank=True)
    twitter = models.CharField(max_length=60, null=True, blank=True)
    youtube = models.CharField(max_length=60, null=True, blank=True)
    whatsapp = models.CharField(max_length=60, null=True, blank=True)
    pinterest = models.CharField(max_length=60, null=True, blank=True)

    @property
    def full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_contact_data(self):
        return f"email: {self.email}\nphone_number: {self.phone_number}\nfull_name: {self.full_name}"

    def add_subscription(self, days_number: int):
        if not self.subscribe_until_date:
            self.subscribe_until_date = timezone.now() + timezone.timedelta(days=days_number)
        elif self.subscribe_until_date <= timezone.now():
            self.subscribe_until_date = timezone.now() + timezone.timedelta(days=days_number)
        else:
            self.subscribe_until_date += timezone.timedelta(days=days_number)

    @property
    def get_subscription(self):
        """
        WARNING!! NOT CODE DELETE!

        the first six months the site works without subscriptions
        commented code is left for the future!!!!!
        :return:
        """
        return True

        # customer = Customer.objects.filter(subscriber=self).first()
        # if not customer:
        #     return False
        # if customer.active_subscriptions:
        #     return True
        # return False

    @property
    def get_photo_url(self):
        if self.profile_image:
            return self.profile_image.url
        else:
            return "/static/images/user.png"

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


class CounterStrMixin:

    def __str__(self):
        return self.name

    @property
    def get_count(self):
        return self.sale_ads.count()


class ChoicesMixin:
    @classmethod
    def get_choices(cls):
        return [(tq.pk, tq.name) for tq in cls.objects.order_by('name').all()]


class ModelTrack(models.Model, ChoicesMixin):
    name = models.CharField(max_length=120)

    class Meta:
        verbose_name_plural = "trailers model"

    def __str__(self):
        return self.name

    @property
    def get_count(self):
        return self.sale_ads.count()


class CategoriesTrack(models.Model, ChoicesMixin):
    image = models.ImageField(upload_to="category_images/", null=True)
    name = models.SlugField(unique=True, db_index=True)

    def __str__(self):
        return self.name

    @property
    def get_image_url(self):
        if self.image:
            return self.image.url
        else:
            return "/static/images/user.png"

    @property
    def get_count(self):
        return self.sale_ads.count()


class MakeTrack(models.Model, ChoicesMixin):
    name = models.CharField(max_length=120)

    class Meta:
        verbose_name_plural = "trailers make"

    def __str__(self):
        return self.name

    @property
    def get_count(self):
        return self.sale_ads.count()


class ShouldInclude(models.Model, ChoicesMixin):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

    @property
    def get_count(self):
        return self.sale_ads.count()


class TypeOfTrailer(models.Model, ChoicesMixin):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

    @property
    def get_count(self):
        return self.sale_ads.count()


class SizeOfTrailer(models.Model, ChoicesMixin):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

    @property
    def get_count(self):
        return self.sale_ads.count()


class Suspension(models.Model, ChoicesMixin):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

    @property
    def get_count(self):
        return self.sale_ads.count()


class TruckModel(models.Model, ChoicesMixin):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

    @property
    def get_count(self):
        return self.sale_ads.count()


class TruckMake(models.Model, ChoicesMixin):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

    @property
    def get_count(self):
        return self.sale_ads.count()


class SaleAds(models.Model):
    class Meta:
        ordering = ('-created_at',)

    title = models.CharField(max_length=120, null=True)
    check_engine_warning_lights = models.TextField(max_length=5000, null=True, blank=True)
    type_of_5_wheel = models.CharField(max_length=500, null=True, blank=True)
    jake_brake = models.CharField(max_length=500, null=True, blank=True)
    wheel_base = models.CharField(max_length=500, null=True, blank=True)
    number_of_aluminum_wheels = models.CharField(max_length=500, null=True, blank=True)
    tire_size = models.CharField(max_length=120, null=True, blank=True)
    any_know_problems_with_vehicle = models.TextField(max_length=5000, null=True, blank=True)
    sleeper_size = models.CharField(max_length=120, null=True, blank=True)

    tire_percent_front_right = models.PositiveIntegerField(default=50,
                                                           validators=[MinValueValidator(1), MaxValueValidator(100)])
    tire_percent_front_left = models.PositiveIntegerField(default=50,
                                                          validators=[MinValueValidator(1), MaxValueValidator(100)])
    tire_percent_rear_left = models.PositiveIntegerField(default=50,
                                                         validators=[MinValueValidator(1), MaxValueValidator(100)])
    tire_percent_rear_right = models.PositiveIntegerField(default=50,
                                                          validators=[MinValueValidator(1), MaxValueValidator(100)])
    tire_percent_rear_drive_tires = models.PositiveIntegerField(default=50,
                                                                validators=[MinValueValidator(1),
                                                                            MaxValueValidator(100)])

    vehicle_year = models.DateField(null=True, blank=True)
    vehicle_fuel = models.CharField(max_length=60, null=True, blank=True)

    vehicle_price_amount = models.PositiveIntegerField(default=1000, null=True)

    vehicle_condition = models.CharField(max_length=60, null=True, blank=True)
    description = models.TextField(max_length=5000, null=True, blank=True)
    preview_image = models.ImageField(upload_to="images/", null=True, blank=True)

    vehicle_mileage = models.PositiveIntegerField(default=1000, null=True, blank=True)
    phone_number = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(max_length=120, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='sale_ads')
    vehicle_make = models.ForeignKey(MakeTrack, on_delete=models.SET_NULL, related_name='sale_ads', null=True,
                                     blank=True)
    vehicle_model = models.ForeignKey(ModelTrack, on_delete=models.SET_NULL, related_name='sale_ads', null=True,
                                      blank=True)
    vehicle_category = models.ForeignKey(CategoriesTrack, on_delete=models.SET_NULL, related_name='sale_ads', null=True,
                                         blank=True)
    should_include = models.ForeignKey(ShouldInclude, on_delete=models.SET_NULL, related_name='sale_ads', null=True,
                                       blank=True)

    # Trailer part

    type_of_5_trailer = models.ForeignKey(TypeOfTrailer, on_delete=models.SET_NULL, related_name='sale_ads', null=True,
                                          blank=True)
    size_of_trailer = models.ForeignKey(SizeOfTrailer, on_delete=models.SET_NULL, related_name='sale_ads', null=True,
                                        blank=True)

    suspension = models.ForeignKey(Suspension, on_delete=models.SET_NULL, related_name='sale_ads', null=True,
                                   blank=True)
    truck_make = models.ForeignKey(TruckMake, on_delete=models.SET_NULL, related_name='sale_ads', null=True, blank=True)
    truck_model = models.ForeignKey(TruckModel, on_delete=models.SET_NULL, related_name='sale_ads', null=True,
                                    blank=True)
    length = models.PositiveIntegerField(default=1000, null=True, blank=True)
    width = models.PositiveIntegerField(default=1000, null=True, blank=True)
    height = models.PositiveIntegerField(default=1000, null=True, blank=True)
    air_ride = models.CharField(max_length=120, null=True, blank=True)
    capacity_of_trailer = models.CharField(max_length=120, null=True, blank=True)
    hours_if_applicable = models.CharField(max_length=120, null=True, blank=True)

    roof_type = models.CharField(max_length=120, null=True, blank=True)
    trailer_lining = models.CharField(max_length=120, null=True, blank=True)

    virgin_tires_or_recapped = models.CharField(max_length=120, null=True, blank=True)

    # Auction part
    sales = models.BooleanField(default=False)
    last_price = models.PositiveIntegerField(default=0, null=True)
    sale_end_time = models.DateTimeField(default=django.utils.timezone.now)
    user_bet = models.ForeignKey(MyUser, on_delete=models.SET_NULL, related_name='auction_bet', null=True, blank=True)
    user_watch = models.ManyToManyField(MyUser, related_name='auction_watch', null=True, blank=True)
    send_email_to_winner = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} by {self.user}"

    @property
    def time_auction_left(self):
        if timezone.now() >= self.sale_end_time:
            return True
        return False

    def is_user_watch(self, user_obj):
        if self.user_watch.filter(id=user_obj.pk).exists():
            return True
        return False

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
    def get_last_hours(self):
        if self.sale_end_time > timezone.now():
            time_left = str(self.sale_end_time - timezone.now())
            return time_left.split(".")[0]

    @property
    def is_used(self):
        if self.vehicle_condition == "Used":
            return True
        return False

    @property
    def get_photo_url(self):
        if self.preview_image:
            return self.preview_image.url
        else:
            return "/static/images/user.png"

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
    email_1 = models.EmailField(null=True, default="info@bymyfleet.net")
    email_2 = models.EmailField(null=True, default="info@bymyfleet.net")
    phone_number_1 = models.CharField(null=True, max_length=120, default="(260) 888-2323")
    phone_number_2 = models.CharField(null=True, max_length=120, default="(260) 888-2323")
    address_top = models.CharField(null=True, max_length=120, default="1Hd- 50, 010 Avenue")
    address_bottom = models.CharField(null=True, max_length=120, default="NY 90001 United States")
    news_letter_title = models.CharField(null=True, max_length=120, default="Our Newsletter")
    news_letter_text = models.CharField(null=True, max_length=300,
                                        default="Be the first to know about our offers and discounts by subscribing to the newsletter")


class SettingsHeaderHome(models.Model):
    header_title = models.CharField(null=True, max_length=120, default="Used Equipment or Sale")
    header_text = models.CharField(null=True, max_length=500,
                                   default="An Online Auction for your used Trucks and Trailers")
    contact_email = models.EmailField(null=True, default="info@example.com")
    contact_number = models.CharField(null=True, max_length=120, default="+91 987-654-3210")


class IsNotSingleHeaderMixin:
    @property
    def is_not_single_header(self):
        return True


class SingleModelMixin:
    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)


class SettingsAuthBase(models.Model):
    title = models.TextField(default="Lorem ipsum dolor sit amet consectetur adipisicing")
    text = models.TextField(
        default="Elit Iusto dolore libero recusandae dolor dolores explicabo ullam cum facilis aperiam alias odio quam excepturi molestiae omnis inventore. Repudiandae officiaplaceat amet consectetur dicta dolorem quo")


class SettingsHeaderInventoryGrid(models.Model, IsNotSingleHeaderMixin):
    inventory_title = models.TextField(default="Inventory Grid View")
    inventory_link_name = models.TextField(default="Inventory Grid")


class SettingsHeaderContact(models.Model, IsNotSingleHeaderMixin):
    inventory_title = models.TextField(default="contact us")
    inventory_link_name = models.TextField(default="Contact")


class FaqHeader(models.Model, IsNotSingleHeaderMixin):
    inventory_title = models.TextField(default="faq")
    inventory_link_name = models.TextField(default="Faq")


class SettingsHeaderInventoryCatalog(models.Model, IsNotSingleHeaderMixin):
    inventory_title = models.TextField(default="Inventory Catalog View")
    inventory_link_name = models.TextField(default="Inventory Catalog")


class SettingsHeaderInventorySingle(models.Model):
    inventory_title = models.TextField(default="Inventory Single Page")
    inventory_link_name = models.TextField(default="Inventory List")
    inventory_single_page = models.TextField(default="Inventory Single")


class SettingsHeaderAboutUs(models.Model, IsNotSingleHeaderMixin):
    inventory_title = models.TextField(default="About our company")
    inventory_link_name = models.TextField(default="About-Us")


class SettingsHeaderPrivacy(models.Model, IsNotSingleHeaderMixin):
    inventory_title = models.TextField(default="Privacy Policy")
    inventory_link_name = models.TextField(default="Privacy")


class SettingsHeaderTerms(models.Model, IsNotSingleHeaderMixin):
    inventory_title = models.TextField(default="Terms conditions")
    inventory_link_name = models.TextField(default="Terms")


class SettingsIndexHome(models.Model):
    part_start_title = models.TextField(default="find categories")
    part_start_text = models.TextField(default="Lorem ipsum dolor sit amet consectetur adipisicing")
    part_features_title = models.TextField(default="our featured listing")
    part_features_text = models.TextField(default="Lorem ipsum dolor sit amet consectetur adipisicin")
    brand_part_title = models.TextField(default="browse by make")
    brand_part_text = models.TextField(default="Lorem ipsum dolor sit amet consectetur adipisicin")
    price_part_title = models.TextField(default="our ads pricing plans")
    price_part_text = models.TextField(default="Lorem ipsum dolor sit amet consectetur adipisicin")
    recent_part_title = models.TextField(default="recently added")
    recent_part_text = models.TextField(default="not displayed")


class FakeReviewIndexHome(models.Model):
    name_sale = models.TextField(default="Lorem ipsum dolor sit amet consectetur adipisicin")
    review_title = models.TextField(default="Lorem ipsum dolor sit amet consectetur adipisicin")
    review_text = models.TextField(default="Lorem ipsum dolor sit amet consectetur adipisicin")
    review_author = models.TextField(default="Lorem ipsum dolor sit amet consectetur adipisicin")
    review_author_red_text = models.TextField(default="Lorem ipsum dolor sit amet consectetur adipisicin")
    image = models.ImageField(null=True, upload_to="settings_images/")

    def __str__(self):
        return f'fake_review {self.name_sale}'

    @property
    def get_image_url(self):
        if self.image:
            return self.image.url
        else:
            return "/media/settings_images/02.jpg"
