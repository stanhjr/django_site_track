from django.urls import path

from site_track.views import ContactView, IndexView, InventoryGridView, InventoryCatalogView, AboutUs, Privacy, FaqView

urlpatterns = [
    path('contact/', ContactView.as_view(), name='contact'),
    path('', IndexView.as_view(), name='home'),
    path('category/<slug:category>', InventoryGridView.as_view(), name='inventory-grid'),
    path('catalog/', InventoryCatalogView.as_view(), name='catalog'),
    path('faq/', FaqView.as_view(), name='faq'),
    path('about_us/', AboutUs.as_view(), name='about-us'),
    path('privacy/', Privacy.as_view(), name='privacy'),

]
