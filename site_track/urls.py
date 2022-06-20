from django.urls import path

from site_track.views import ContactView, IndexView

urlpatterns = [
    path('contact/', ContactView.as_view(), name='contact'),
    path('', IndexView.as_view(), name='home'),

]
