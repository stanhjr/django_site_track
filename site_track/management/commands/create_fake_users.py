import random

from faker import Faker
import factory
from django.db import transaction
from factory.django import DjangoModelFactory

from django.core.management.base import BaseCommand

from site_track.models import MyUser, CategoriesTrack, MakeTrack

ava_random = ("fake_avatar/01.jpg", "fake_avatar/02.jpg", "fake_avatar/03.jpg", "fake_avatar/04.jpg",
              "fake_avatar/05.jpg", "fake_avatar/06.jpg", "fake_avatar/07.jpg")

users_random = MyUser.objects.exclude(username="stan").all()

random_category = CategoriesTrack.objects.all()
random_make = MakeTrack.objects.all()

faker = Faker()


class UserFactory(DjangoModelFactory):
    class Meta:
        model = MyUser


class Command(BaseCommand):
    help = "genetating fake data"

    @transaction.atomic
    def handle(self, *args, **options):
        self.stdout.write("Creating fake data")

        for _ in range(35):
            UserFactory(email=faker.email(),
                        username=faker.email(),
                        profile_image=random.choice(ava_random),
                        account_name=faker.name(),
                        phone_number=faker.phone_number(),
                        full_name=faker.name(),
                        country="USA",
                        state=faker.text()[1:10],
                        zip=str(faker.random_int(1000, 5000)),
                        about_vendor=faker.text()[:200],
                        )
