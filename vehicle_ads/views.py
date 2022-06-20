from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy

from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView, TemplateView

from site_track.models import SaleAds, ImageInGallery
from vehicle_ads.forms import VehicleInformationForm, VehicleInformationUpdateForm


class VehicleInformationView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = SaleAds
    template_name = 'create-ads.html'
    success_url = reverse_lazy('create-sale-ads')
    form_class = VehicleInformationForm

    def get_form_kwargs(self):
        kw = super(VehicleInformationView, self).get_form_kwargs()
        kw['request'] = self.request
        return kw

    def form_invalid(self, form):
        return redirect('create-sale-ads')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user

        # obj.user.save()
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

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return super().get_queryset().filter(user=self.request.user)
        return super().get_queryset()

    def handle_no_permission(self):
        return redirect('login')


class UserPostedAdsDeleteView(LoginRequiredMixin, DeleteView):
    model = SaleAds
    success_url = reverse_lazy('user-posted-sale-ads')


class UserPostedAdsUpdateView(LoginRequiredMixin, UpdateView):
    model = SaleAds
    success_url = reverse_lazy('user-posted-sale-ads')
    template_name = 'update-ads.html'
    form_class = VehicleInformationUpdateForm

    def dispatch(self, *args, **kwargs):
        obj = self.get_object()
        if self.request.user.id != obj.user.id:
            redirect('user-posted-sale-ads')
        return super(UserPostedAdsUpdateView, self).dispatch(*args, **kwargs)

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


class InventorySingleDetailView(LoginRequiredMixin, DetailView):
    model = SaleAds
    template_name = 'inventory-single.html'

    def get_context_data(self, **kwargs):
        context = super(InventorySingleDetailView, self).get_context_data(**kwargs)
        context['image_gallery'] = ImageInGallery.objects.filter(gallery=self.object).all()
        return context










