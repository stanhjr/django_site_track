from django.contrib import admin
from .models import MyUser, SaleAds, ImageInGallery, SettingsFooter, CategoriesTrack, SettingsHeaderHome, \
    SettingsHeaderInventoryGrid, SettingsHeaderContact, SettingsHeaderInventoryCatalog, SettingsHeaderInventorySingle, \
    SettingsIndexHome, FakeReviewIndexHome, MakeTrack, ModelTrack, TruckMake, TruckModel, TypeOfTrailer, TypeOfTruck, \
    SizeOfTrailer, Suspension, Engine, Horsepower, Transmission, TypeOf5Wheel, TireSize, SleeperSize


class UserSearch(admin.ModelAdmin):
    ordering = ['created_at']
    search_fields = ('email', 'username', 'first_name', 'last_name')


class SaleAdsSearch(admin.ModelAdmin):
    ordering = ['created_at']
    search_fields = ('title', 'user__email')


admin.site.register(TruckMake)
admin.site.register(TruckModel)
admin.site.register(TypeOfTrailer)
admin.site.register(TypeOfTruck)
admin.site.register(MyUser, UserSearch)
admin.site.register(SaleAds, SaleAdsSearch)
admin.site.register(ImageInGallery)
admin.site.register(SettingsFooter)
admin.site.register(CategoriesTrack)
admin.site.register(SettingsHeaderHome)
admin.site.register(SettingsHeaderInventoryGrid)
admin.site.register(SettingsHeaderContact)
admin.site.register(SettingsHeaderInventoryCatalog)
admin.site.register(SettingsHeaderInventorySingle)
admin.site.register(SettingsIndexHome)
admin.site.register(FakeReviewIndexHome)
admin.site.register(MakeTrack)
admin.site.register(ModelTrack)

admin.site.register(SizeOfTrailer)
admin.site.register(Suspension)
admin.site.register(Engine)
admin.site.register(Horsepower)
admin.site.register(Transmission)
admin.site.register(TypeOf5Wheel)
admin.site.register(TireSize)
admin.site.register(SleeperSize)
