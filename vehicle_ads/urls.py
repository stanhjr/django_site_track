"""django_site_track URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from vehicle_ads.views import VehicleInformationView, UserPostedAds, UserPostedAdsDeleteView, UserPostedAdsUpdateView, \
    InventorySingleDetailView, TruckCreateView, UpdateTruckView, TruckDetailView

urlpatterns = [
    path('sale-ads/', VehicleInformationView.as_view(), name='create-sale-ads'),
    path('create-truck/', TruckCreateView.as_view(), name='create-truck'),
    path('update-truck/<pk>', UpdateTruckView.as_view(), name='update-truck'),
    path('posted-ads/', UserPostedAds.as_view(), name='user-posted-sale-ads'),
    path('posted-delete/<pk>', UserPostedAdsDeleteView.as_view(), name='user-posted-delete'),
    path('posted-update/<pk>', UserPostedAdsUpdateView.as_view(), name='user-posted-update'),
    path('posted-detail/<pk>', InventorySingleDetailView.as_view(), name='posted-detail'),
    path('truck-detail/<pk>', TruckDetailView.as_view(), name='truck-detail'),
]
