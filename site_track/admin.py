from django.contrib import admin
from .models import MyUser, SaleAds, ImageInGallery, SettingsFooter

admin.site.register(MyUser)
admin.site.register(SaleAds)
admin.site.register(ImageInGallery)
admin.site.register(SettingsFooter)
# Register your models here.
