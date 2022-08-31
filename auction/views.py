from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import UpdateView, ListView

from auction.forms import AuctionBetForm
from email_sender.tasks import send_buy_now_owner, send_buy_now_customer
from site_track.models import SaleAds, SettingsFooter
from vehicle_ads.views import SubscribeMixin


class AuctionUpdateView(SubscribeMixin, UpdateView):
    model = SaleAds
    form_class = AuctionBetForm

    def form_valid(self, form):
        if not self.request.user.is_authenticated:
            safe_string = reverse('home') + "#price-buy-banner"
            return redirect(safe_string)
        safe_string = reverse_lazy('posted-detail', kwargs={'pk': form.instance.pk})
        obj = form.save(commit=False)

        if obj.sale_end_time > self.request.user.subscribe_until_date:
            messages.success(self.request,
                             'your subscription ends before this auction expires, please renew your subscription')
            return redirect(safe_string)

        if obj.last_price <= self.get_object().last_price:
            messages.success(self.request, 'bet must be greater than the previous one')

            return redirect(safe_string)

        obj.user_bet = self.request.user
        obj.user_watch.add(self.request.user)
        obj.save()

        return redirect(safe_string)


class AuctionBuyNowView(SubscribeMixin, View):
    http_method_names = ['post', ]

    def post(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            safe_string = reverse('home') + "#price-buy-banner"
            return redirect(safe_string)

        sale_ads = SaleAds.objects.filter(pk=kwargs.get("pk")).first()
        if sale_ads.vehicle_category.name.lower() == 'truck':
            safe_string = reverse_lazy('truck-detail', kwargs={'pk': kwargs.get("pk")})
        else:
            safe_string = reverse_lazy('posted-detail', kwargs={'pk': kwargs.get("pk")})

        if self.request.user.subscribe_until_date:
            if sale_ads.sale_end_time > self.request.user.subscribe_until_date and not self.request.user.subscription_one_time:
                messages.success(self.request,
                                 'your subscription ends before this auction expires, please renew your subscription')
                return redirect(safe_string)
        elif not self.request.user.subscribe_until_date and not self.request.user.subscription_one_time:
            messages.success(self.request,
                             'your subscription ends before this auction expires, please renew your subscription')
            return redirect(safe_string)

        if sale_ads:
            sale_ads.sales = True
            sale_ads.user_bet = request.user
            send_buy_now_owner.delay(pk=sale_ads.pk,
                                     email_to=sale_ads.user.email,
                                     contact_data_customer=sale_ads.user_bet.get_contact_data(),
                                     category_name=sale_ads.vehicle_category.name)
            send_buy_now_customer.delay(pk=sale_ads.pk,
                                        email_to=sale_ads.user_bet.email,
                                        contact_data_owner=sale_ads.user.get_contact_data(),
                                        category_name=sale_ads.vehicle_category.name)
            customer = sale_ads.user_bet
            customer.subscription_one_time = False
            customer.save()
            sale_ads.save()

        return redirect(safe_string)


class AuctionWatchView(View):
    http_method_names = ['post', ]

    def post(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            safe_string = reverse('home') + "#price-buy-banner"
            return redirect(safe_string)
        sale_ads = SaleAds.objects.filter(pk=kwargs.get("pk")).first()

        if sale_ads.vehicle_category.name.lower() == 'truck':
            safe_string = reverse_lazy('truck-detail', kwargs={'pk': kwargs.get("pk")})
        else:
            safe_string = reverse_lazy('posted-detail', kwargs={'pk': kwargs.get("pk")})
        if not sale_ads:
            return redirect(safe_string)
        if sale_ads.user_watch.filter(id=request.user.pk):
            sale_ads.user_watch.remove(request.user)
        else:
            sale_ads.user_watch.add(request.user)
        sale_ads.save()
        return redirect(safe_string)


class WatchListView(LoginRequiredMixin, ListView):
    model = SaleAds
    template_name = 'posted-ads.html'
    paginate_by = 16

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(WatchListView, self).get_context_data(**kwargs)
        context['footer'] = SettingsFooter.objects.last()
        context['watch_list'] = True
        context['title'] = 'watch list'
        return context

    def get_queryset(self):
        if self.request.user.is_authenticated:
            result = [obj for obj in super().get_queryset() if obj.is_user_watch(self.request.user)]
            return super().get_queryset().filter(user_watch=self.request.user)
        return super().get_queryset()

    def handle_no_permission(self):
        return redirect('login')
