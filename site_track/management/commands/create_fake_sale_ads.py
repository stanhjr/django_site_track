import random

from faker import Faker

from django.db import transaction
from factory.django import DjangoModelFactory

from django.core.management.base import BaseCommand

from site_track.models import SaleAds, MyUser, ImageInGallery, CategoriesTrack, MakeTrack


preview_random = ("fake_preview/01.jpg", "fake_preview/02.jpg", "fake_preview/03.jpg", "fake_preview/04.jpg",
                  "fake_preview/05.jpg", "fake_preview/06.jpg", "fake_preview/07.jpg", "fake_preview/08.jpg",
                  "fake_preview/09.jpg", "fake_preview/14.jpg", "fake_preview/15.jpg",
                  "fake_preview/11.jpg", "fake_preview/12.jpg", "fake_preview/13.jpg", "fake_preview/10.jpg")

users_random = MyUser.objects.all()

random_category = CategoriesTrack.objects.all()
random_model = MakeTrack.objects.all()
random_make = MakeTrack.objects.all()

VEHICLE_FUEL_CHOICES = ("Diesel", "Petrol", "Electric", "Electric", "Hybrid")


VEHICLE_CONDITION_CHOICES = ("New", "Used")


faker = Faker()


class ImageInGalleryFactory(DjangoModelFactory):
    class Meta:
        model = ImageInGallery


class SaleAdsFactory(DjangoModelFactory):
    class Meta:
        model = SaleAds

    preview_image = random.choice(preview_random)


class Command(BaseCommand):
    help = "genetating fake data"

    @transaction.atomic
    def handle(self, *args, **options):
        self.stdout.write("Creating fake data")

        for _ in range(5000):
            SaleAdsFactory(vehicle_category=random.choice(random_category),
                           vehicle_model=random.choice(random_model),
                           vehicle_make=random.choice(random_make),
                           user=random.choice(users_random),
                           title=faker.text()[1:50],
                           preview_image=random.choice(preview_random),
                           check_engine_warning_lights=faker.text()[:20],
                           type_of_5_wheel=faker.text()[:20],
                           jake_brake=faker.text()[:10],
                           wheel_base=faker.text()[:10],
                           number_of_aluminum_wheels=faker.text()[:10],
                           tire_size=faker.random_int(1, 8),
                           any_know_problems_with_vehicle=faker.text(),
                           sleeper_size=faker.text()[:10],
                           tire_percent_front_left=faker.random_int(1, 100),
                           tire_percent_front_right=faker.random_int(1, 100),
                           tire_percent_rear_left=faker.random_int(1, 100),
                           tire_percent_rear_right=faker.random_int(1, 100),
                           tire_percent_rear_drive_tires=faker.random_int(1, 100),
                           vehicle_year=faker.date_of_birth(),
                           vehicle_fuel=random.choice(VEHICLE_FUEL_CHOICES),
                           vehicle_price_amount=faker.random_int(1000, 30000),
                           vehicle_condition=random.choice(VEHICLE_CONDITION_CHOICES),
                           description=faker.text(),
                           vehicle_mileage=faker.random_int(1000, 100000),
                           )
