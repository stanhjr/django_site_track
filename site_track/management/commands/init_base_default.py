from django.core.management.base import BaseCommand
from site_track.models import FakeReviewIndexHome, SettingsHeaderInventoryGrid, SettingsAuthBase, \
    SettingsHeaderInventoryCatalog, SettingsHeaderInventorySingle, SettingsFooter, SettingsIndexHome, \
    SettingsHeaderAboutUs, SettingsHeaderPrivacy, SettingsHeaderContact, CategoriesTrack, MakeTrack, ModelTrack, \
    FaqHeader, TruckMake, TruckModel, SpringRide, TypeOfTrailer, ShouldInclude, SettingsHeaderTerms


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

        if not SettingsHeaderTerms.objects.last():
            SettingsHeaderTerms.objects.create()

        if not SettingsHeaderContact.objects.last():
            SettingsHeaderContact.objects.create()

        if not FaqHeader.objects.last():
            FaqHeader.objects.create()

        if not CategoriesTrack.objects.last():
            CategoriesTrack.objects.create(name="Truck", image="category_images/jeep.png")
            CategoriesTrack.objects.create(name="Trailer", image="category_images/hatchback.png")

        if not TruckMake.objects.last():
            TruckMake.objects.create(name="Truck Make 1")
            TruckMake.objects.create(name="Truck Make 2")
            TruckMake.objects.create(name="Truck Make 3")

        if not TruckModel.objects.last():
            TruckModel.objects.create(name="Truck Model  1")
            TruckModel.objects.create(name="Truck Model  2")
            TruckModel.objects.create(name="Truck Model  3")

        if not SpringRide.objects.last():
            SpringRide.objects.create(name="Spring Ride 1")
            SpringRide.objects.create(name="Spring Ride 2")
            SpringRide.objects.create(name="Spring Ride 3")
            SpringRide.objects.create(name="Spring Ride 4")
            SpringRide.objects.create(name="Spring Ride 5")

        if not TypeOfTrailer.objects.last():
            TypeOfTrailer.objects.create(name="Type Of  1")
            TypeOfTrailer.objects.create(name="Type Of  2")
            TypeOfTrailer.objects.create(name="Type Of  3")

        if not ShouldInclude.objects.last():
            ShouldInclude.objects.create(name="Should 1")
            ShouldInclude.objects.create(name="Should 2")
            ShouldInclude.objects.create(name="Should 3")
            ShouldInclude.objects.create(name="Should 4")
            ShouldInclude.objects.create(name="Should 5")
            ShouldInclude.objects.create(name="Should 6")



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
