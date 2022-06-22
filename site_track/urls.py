from django.urls import path

from site_track.views import ContactView, IndexView, InventoryGridView, InventoryCatalogView

urlpatterns = [
    path('contact/', ContactView.as_view(), name='contact'),
    path('', IndexView.as_view(), name='home'),
    path('category/<slug:category>', InventoryGridView.as_view(), name='inventory-grid'),
    path('catalog/', InventoryCatalogView.as_view(), name='catalog'),

]
