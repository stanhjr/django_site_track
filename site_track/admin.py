from django.contrib import admin
from .models import MyUser, SaleAds, ImageInGallery, SettingsFooter, CategoriesTrack

admin.site.register(MyUser)
admin.site.register(SaleAds)
admin.site.register(ImageInGallery)
admin.site.register(SettingsFooter)
admin.site.register(CategoriesTrack)
# Register your models here.
