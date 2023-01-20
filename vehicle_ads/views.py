from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse

from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
from djstripe.models import Customer

from auction.forms import AuctionBetForm
from core.utils import is_need_subscribe
from django_site_track.settings import STRIPE_PLAN
from email_sender.tasks import send__make_offer_mail
from site_track.models import SaleAds, ImageInGallery, SettingsFooter, SettingsHeaderInventorySingle, CategoriesTrack

from vehicle_ads.forms import TruckCreateForm, TruckUpdateForm, TrailerUpdateForm, TrailerCreateForm


class SubscribeMixin:
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            safe_string = reverse('home') + "#price-buy-banner"
            return redirect(safe_string)
        if not self.request.user.get_subscription:
            safe_string = reverse('home') + "#price-buy-banner"
            return redirect(safe_string)
        return super().dispatch(request, *args, **kwargs)


class VehicleInformationView(LoginRequiredMixin, SubscribeMixin, CreateView):
    login_url = reverse_lazy('login')
    model = SaleAds
    template_name = 'create-ads.html'
    success_url = reverse_lazy('create-sale-ads')
    form_class = TruckCreateForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(VehicleInformationView, self).get_context_data(**kwargs)
        context['footer'] = SettingsFooter.objects.last()
        context['active_create_ads'] = True
        context['title'] = 'create ads'
        return context

    def get_form_kwargs(self):
        kw = super(VehicleInformationView, self).get_form_kwargs()
        kw['request'] = self.request
        return kw

    def form_invalid(self, form):
        return redirect('create-sale-ads')

    def form_valid(self, form):
        obj = form.save(commit=False)
        customer_stripe, _ = Customer.get_or_create(subscriber=self.request.user)
        if is_need_subscribe() and not customer_stripe.is_subscribed_to(STRIPE_PLAN):
            messages.success(self.request,
                             f'your subscription ends before the end of the auction, your subscription will expire')
            safe_string = reverse('home') + "#price-buy-banner"
            return redirect(safe_string)

        obj.user = self.request.user
        obj.vehicle_category = CategoriesTrack.objects.filter(name='Trailer').first()
        obj.save()
        images = self.request.FILES.getlist("gallery-image")
        for image in images:
            image_obj = ImageInGallery.objects.create(image=image, gallery=obj)
            obj.image_in_gallery.add(image_obj, bulk=False)
        obj.save()
        user = self.request.user
        user.subscription_one_time = False
        user.save()
        return super().form_valid(form=form)


class TruckCreateView(LoginRequiredMixin, SubscribeMixin, CreateView):
    login_url = reverse_lazy('login')
    model = SaleAds
    template_name = 'create_truck.html'
    success_url = reverse_lazy('create-truck')
    form_class = TrailerCreateForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TruckCreateView, self).get_context_data(**kwargs)
        context['footer'] = SettingsFooter.objects.last()
        context['active_create_truck'] = True
        context['title'] = 'create trailer'
        return context

    def get_form_kwargs(self):
        kw = super(TruckCreateView, self).get_form_kwargs()
        kw['request'] = self.request
        return kw

    def form_invalid(self, form):
        return redirect('create-truck')

    def form_valid(self, form):
        obj = form.save(commit=False)
        customer_stripe, _ = Customer.get_or_create(subscriber=self.request.user)
        if is_need_subscribe() and not customer_stripe.is_subscribed_to(STRIPE_PLAN):
            messages.success(self.request,
                             f'your subscription ends before the end of the auction, your subscription will expire')
            safe_string = reverse('home') + "#price-buy-banner"
            return redirect(safe_string)
        obj.vehicle_category = CategoriesTrack.objects.filter(name='Truck').first()
        obj.user = self.request.user
        obj.save()
        images = self.request.FILES.getlist("gallery-image")
        for image in images:
            image_obj = ImageInGallery.objects.create(image=image, gallery=obj)
            obj.image_in_gallery.add(image_obj, bulk=False)
        obj.save()
        user = self.request.user
        user.subscription_one_time = False
        user.save()

        return super().form_valid(form=form)


class UserPostedAds(LoginRequiredMixin, ListView):
    model = SaleAds
    template_name = 'posted-ads.html'
    paginate_by = 16

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserPostedAds, self).get_context_data(**kwargs)
        context['footer'] = SettingsFooter.objects.last()
        context['active_posted_ads'] = True
        context['title'] = 'posted ads'
        return context

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return super().get_queryset().filter(user=self.request.user)
        return super().get_queryset()

    def handle_no_permission(self):
        return redirect('login')


class UserPostedAdsDeleteView(LoginRequiredMixin, DeleteView):
    model = SaleAds
    success_url = reverse_lazy('user-posted-sale-ads')

    def post(self, request, *args, **kwargs):
        model = self.model.objects.filter(id=kwargs.get("pk")).first()
        if model.user == self.request.user or request.user.is_superuser:
            return super().post(self, request, *args, **kwargs)
        return redirect('home')


class UserPostedAdsUpdateView(LoginRequiredMixin, SubscribeMixin, UpdateView):
    model = SaleAds
    success_url = reverse_lazy('user-posted-sale-ads')
    template_name = 'update-ads.html'
    form_class = TruckUpdateForm

    def dispatch(self, *args, **kwargs):
        obj = self.get_object()
        if self.request.user.id != obj.user.id or not self.request.user.is_superuser:
            redirect('user-posted-sale-ads')
        return super(UserPostedAdsUpdateView, self).dispatch(*args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserPostedAdsUpdateView, self).get_context_data(**kwargs)
        context['footer'] = SettingsFooter.objects.last()
        context['title'] = 'update sale ads'
        return context

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        if self.request.user.id != obj.user.id:
            redirect('user-posted-sale-ads')
        return super(UserPostedAdsUpdateView, self).get(request, *args, **kwargs)

    def get_form_kwargs(self):
        kw = super(UserPostedAdsUpdateView, self).get_form_kwargs()
        kw['request'] = self.request
        return kw

    def get_initial(self):
        habit_object = self.get_object()
        return habit_object.__dict__


class UpdateTruckView(LoginRequiredMixin, SubscribeMixin, UpdateView):
    model = SaleAds
    success_url = reverse_lazy('user-posted-sale-ads')
    template_name = 'update_truck.html'
    form_class = TrailerUpdateForm

    def dispatch(self, *args, **kwargs):
        obj = self.get_object()
        if self.request.user.id != obj.user.id or not self.request.user.is_superuser:
            redirect('user-posted-sale-ads')
        return super(UpdateTruckView, self).dispatch(*args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UpdateTruckView, self).get_context_data(**kwargs)
        context['footer'] = SettingsFooter.objects.last()
        context['title'] = 'update sale ads'
        return context

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        if self.request.user.id != obj.user.id:
            redirect('user-posted-sale-ads')
        return super(UpdateTruckView, self).get(request, *args, **kwargs)

    def get_form_kwargs(self):
        kw = super(UpdateTruckView, self).get_form_kwargs()
        kw['request'] = self.request
        return kw

    def get_initial(self):
        habit_object = self.get_object()
        return habit_object.__dict__


class InventorySingleDetailView(DetailView):
    login_url = reverse_lazy('login')
    model = SaleAds
    template_name = 'inventory-single.html'

    def get_success_url(self):
        return reverse_lazy('catalog')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_user_watch'] = self.object.is_user_watch(self.request.user)
        context['auction_bet_form'] = AuctionBetForm()
        context['image_gallery'] = ImageInGallery.objects.filter(gallery=self.object).all()
        context['footer'] = SettingsFooter.objects.last()
        context['header'] = SettingsHeaderInventorySingle.objects.last()
        # context['send_vendor_mail_form'] = self.get_form()
        context['title'] = 'inventory single'
        context['grid_name'] = self.get_object().title
        return context


    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            send__make_offer_mail.delay(first_name=self.request.POST.get("first_name"),
                                        email_to=self.request.POST['vendor_email'],
                                        email_from=self.request.POST.get("email"),
                                        text=self.request.POST.get("describe_your_message"),
                                        phone_number=self.request.POST.get("phone_number"),
                                        price=self.request.POST.get("enter_your_offer_price"))
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class TruckDetailView(DetailView):
    login_url = reverse_lazy('login')
    model = SaleAds
    template_name = 'truck_single.html'

    def get_success_url(self):
        return reverse_lazy('catalog')

    def get_context_data(self, **kwargs):
        context = super(TruckDetailView, self).get_context_data(**kwargs)
        context['is_user_watch'] = self.object.is_user_watch(self.request.user)
        context['auction_bet_form'] = AuctionBetForm()
        context['image_gallery'] = ImageInGallery.objects.filter(gallery=self.object).all()
        context['footer'] = SettingsFooter.objects.last()
        context['header'] = SettingsHeaderInventorySingle.objects.last()
        context['title'] = 'inventory single'
        context['grid_name'] = self.get_object().title
        return context
