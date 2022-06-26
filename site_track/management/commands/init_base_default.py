from django.core.management.base import BaseCommand
from site_track.models import FakeReviewIndexHome, SettingsHeaderInventoryGrid, SettingsAuthBase, \
    SettingsHeaderInventoryCatalog, SettingsHeaderInventorySingle, SettingsFooter, SettingsIndexHome, \
    SettingsHeaderAboutUs, SettingsHeaderPrivacy, SettingsHeaderContact, CategoriesTrack, MakeTrack


class Command(BaseCommand):
    def handle(self, *args, **options):
        if not FakeReviewIndexHome.objects.last():
            FakeReviewIndexHome.objects.create(name_sale="mercedes-benz wagon",
                                               review_title="see the full review",
                                               review_text="Lorem ipsum dolor sit amet consectetur adipisicing elit Expedita ut porro beatae itaque accusantium nisi Asperiores reprehenderit",
                                               review_author="miron mahmud",
                                               review_author_red_text="buyer review",
                                               image="settings_images/01.jpg")

            FakeReviewIndexHome.objects.create(name_sale="lamborghini huracan",
                                               review_title="see the full review",
                                               review_text="Lorem ipsum dolor sit amet consectetur adipisicing elit Expedita ut porro beatae itaque accusantium nisi Asperiores reprehenderit",
                                               review_author="tahmina bonny",
                                               review_author_red_text="seller review<",
                                               image="settings_images/02.jpg")


        if not SettingsHeaderInventoryGrid.objects.last():
            SettingsHeaderInventoryGrid.objects.create()

        if not SettingsAuthBase.objects.last():
            SettingsAuthBase.objects.create()

        if not SettingsHeaderInventoryCatalog.objects.last():
            SettingsHeaderInventoryCatalog.objects.create()

        if not SettingsHeaderInventorySingle.objects.last():
            SettingsHeaderInventorySingle.objects.create()

        if not SettingsFooter.objects.last():
            SettingsFooter.objects.create()

        if not SettingsIndexHome.objects.last():
            SettingsIndexHome.objects.create()

        if not SettingsHeaderAboutUs.objects.last():
            SettingsHeaderAboutUs.objects.create()

        if not SettingsHeaderPrivacy.objects.last():
            SettingsHeaderPrivacy.objects.create()

        if not SettingsHeaderContact.objects.last():
            SettingsHeaderContact.objects.create()

        if not CategoriesTrack.objects.last():
            CategoriesTrack.objects.create(name="Track", image="category_images/jeep.png")
            CategoriesTrack.objects.create(name="Trailer", image="category_images/hatchback.png")

        if not MakeTrack.objects.last():
            MakeTrack.objects.create(name="classic")
            MakeTrack.objects.create(name="cascade")
            MakeTrack.objects.create(name="coronado")