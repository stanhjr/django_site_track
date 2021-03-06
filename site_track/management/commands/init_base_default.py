from django.core.management.base import BaseCommand
from site_track.models import FakeReviewIndexHome, SettingsHeaderInventoryGrid, SettingsAuthBase, \
    SettingsHeaderInventoryCatalog, SettingsHeaderInventorySingle, SettingsFooter, SettingsIndexHome, \
    SettingsHeaderAboutUs, SettingsHeaderPrivacy, SettingsHeaderContact, CategoriesTrack, MakeTrack, ModelTrack


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
            MakeTrack.objects.create(name="Ford")
            MakeTrack.objects.create(name="Freightliner")
            MakeTrack.objects.create(name="International")
            MakeTrack.objects.create(name="Kenworth")
            MakeTrack.objects.create(name="Peterbilt")
            MakeTrack.objects.create(name="Volvo")
            MakeTrack.objects.create(name="Western Star")

        if not ModelTrack.objects.last():
            ModelTrack.objects.create(name="357")
            ModelTrack.objects.create(name="379")
            ModelTrack.objects.create(name="389")
            ModelTrack.objects.create(name="4300")
            ModelTrack.objects.create(name="4900FA")
            ModelTrack.objects.create(name="579")
            ModelTrack.objects.create(name="Cascadia")
            ModelTrack.objects.create(name="Cascadia 113")
            ModelTrack.objects.create(name="Cascadia 125")
            ModelTrack.objects.create(name="Cascadia Evolution")
            ModelTrack.objects.create(name="Columbia")
            ModelTrack.objects.create(name="Coronado")
            ModelTrack.objects.create(name="F250")
            ModelTrack.objects.create(name="M2")
            ModelTrack.objects.create(name="M2 108SD Crew Cab")
            ModelTrack.objects.create(name="T270")
            ModelTrack.objects.create(name="T370")
            ModelTrack.objects.create(name="T680")
            ModelTrack.objects.create(name="Transit 250")
            ModelTrack.objects.create(name="VNL64T300")
            ModelTrack.objects.create(name="VNL670")
