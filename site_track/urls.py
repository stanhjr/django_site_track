from django.urls import path

from site_track.views import ContactView

urlpatterns = [
    path('contact/', ContactView.as_view(), name='contact'),

]
