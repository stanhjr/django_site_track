from django.urls import path

from .views import AuctionUpdateView, AuctionBuyNowView, AuctionWatchView, WatchListView

urlpatterns = [
    path('buy_now/<pk>', AuctionBuyNowView.as_view(), name='auction-buy-now'),
    path('bet/<pk>', AuctionUpdateView.as_view(), name='auction-bet'),
    path('add_to_watch/<pk>', AuctionWatchView.as_view(), name='add-watch'),
    path('watch_list', WatchListView.as_view(), name='watch-list'),

]