from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse

from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
from django.views.generic.edit import FormMixin

from email_sender.tasks import send__make_offer_mail
from site_track.models import SaleAds, ImageInGallery, SettingsFooter, SettingsHeaderInventoryGrid, \
    SettingsHeaderInventorySingle
from vehicle_ads.forms import VehicleInformationForm, VehicleInformationUpdateForm, SendEmailVendorForm


class VehicleInformationView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = SaleAds
    template_name = 'create-ads.html'
    success_url = reverse_lazy('create-sale-ads')
    form_class = VehicleInformationForm

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
        obj.user = self.request.user
        obj.save()
        images = self.request.FILES.getlist("gallery-image")
        for image in images:
            image_obj = ImageInGallery.objects.create(image=image, gallery=obj)
            obj.image_in_gallery.add(image_obj, bulk=False)
        obj.save()
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


class UserPostedAdsUpdateView(LoginRequiredMixin, UpdateView):
    model = SaleAds
    success_url = reverse_lazy('user-posted-sale-ads')
    template_name = 'update-ads.html'
    form_class = VehicleInformationUpdateForm

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


class InventorySingleDetailView(LoginRequiredMixin, FormMixin, DetailView):
    login_url = reverse_lazy('login')
    model = SaleAds
    template_name = 'inventory-single.html'
    form_class = SendEmailVendorForm

    def get_success_url(self):
        return reverse_lazy('catalog')

    def get_context_data(self, **kwargs):
        context = super(InventorySingleDetailView, self).get_context_data(**kwargs)
        context['image_gallery'] = ImageInGallery.objects.filter(gallery=self.object).all()
        context['footer'] = SettingsFooter.objects.last()
        context['header'] = SettingsHeaderInventorySingle.objects.last()
        context['send_vendor_mail_form'] = self.get_form()
        context['title'] = 'inventory single'
        return context

    def get_form_kwargs(self):
        kw = super(InventorySingleDetailView, self).get_form_kwargs()
        kw['request'] = self.request
        return kw

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
