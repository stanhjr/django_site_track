from django.contrib import admin
from .models import MyUser, SaleAds, ImageInGallery, SettingsFooter, CategoriesTrack, SettingsHeaderHome,\
    SettingsHeaderInventoryGrid, SettingsHeaderContact, SettingsHeaderInventoryCatalog, SettingsHeaderInventorySingle,\
    SettingsIndexHome, FakeReviewIndexHome, MakeTrack


class UserSearch(admin.ModelAdmin):
    ordering = ['created_at']
    search_fields = ('email', 'username', 'full_name')


class SaleAdsSearch(admin.ModelAdmin):
    ordering = ['created_at']
    search_fields = ('title', 'user__email')


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

