import urllib.parse

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import FormView, ListView, TemplateView

from site_track.forms import ContactForm
from site_track.models import SaleAds, SettingsFooter, CategoriesTrack, MakeTrack, SettingsIndexHome, \
    SettingsHeaderInventoryGrid, SettingsHeaderInventoryCatalog, SettingsHeaderContact, FakeReviewIndexHome, \
    SettingsHeaderAboutUs, SettingsHeaderPrivacy, ModelTrack
from email_sender.tasks import send_mail_contact_us


class ContactView(LoginRequiredMixin, FormView):
    template_name = 'contact.html'
    success_url = '/'
    form_class = ContactForm

    def handle_no_permission(self):
        return redirect('login')

    def form_valid(self, form):
        send_mail_contact_us.delay(email_from=form.data.get("email"),
                                   subject=form.data.get("subject"),
                                   text=form.data.get("text"))
        return super().form_valid(form=form)

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['footer'] = SettingsFooter.objects.last()
        context['header'] = SettingsHeaderContact.objects.last()
        context['title'] = 'contacts'
        return context


class IndexView(ListView):
    model = SaleAds
    template_name = 'index.html'
    paginate_by = 24

    def dispatch(self, request, *args, **kwargs):
        if self.request.GET.get('header-search'):
            safe_string = urllib.parse.quote_plus(self.request.GET.get('header-search'))
            safe_string = reverse('catalog') + "?header-search=" + safe_string
            return redirect(safe_string)
        return self.get(request, *args, **kwargs)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return super().get_queryset().order_by('-vehicle_price_amount')[:4]
        return super().get_queryset()

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['recent_objects'] = SaleAds.objects.order_by('-created_at')[:4]
        context['footer'] = SettingsFooter.objects.last()
        context['body'] = SettingsIndexHome.objects.last()
        context['category_track'] = CategoriesTrack.objects.annotate(num_children=Count('sale_ads')).order_by(
            '-num_children')[:12]
        context['make_track'] = MakeTrack.objects.annotate(num_children=Count('sale_ads')).order_by('-num_children')[:5]
        context['fake_review'] = FakeReviewIndexHome.objects.all()
        context['title'] = 'home'
        return context


class InventoryGridView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = CategoriesTrack
    template_name = 'inventory-grid.html'
    paginate_by = 24

    def get_queryset(self):
        order_by = self.request.GET.get("order_by")
        search_title = self.request.GET.get("header-search")
        category = self.model.objects.filter(name__icontains=self.kwargs.get("category")).first()
        if category:
            sale_ads = category.sale_ads
        else:
            raise Http404
        model_list = self.request.GET.getlist("model")
        make_list = self.request.GET.getlist("make")
        try:
            price_min = int(self.request.GET.get("price_min"))
        except (ValueError, TypeError):
            price_min = None
        try:
            price_max = int(self.request.GET.get("price_max"))
        except (ValueError, TypeError):
            price_max = None
        if search_title:
            sale_ads = sale_ads.filter(title__exact=search_title)
        if model_list:
            sale_ads = sale_ads.filter(vehicle_model__id__in=model_list)
        if make_list:
            sale_ads = sale_ads.filter(vehicle_make__id__in=make_list)
        if price_max:
            sale_ads = sale_ads.filter(vehicle_price_amount__lte=price_max)
        if price_min:
            sale_ads = sale_ads.filter(vehicle_price_amount__gte=price_min)
        if order_by == "price_up":
            sale_ads = sale_ads.order_by("vehicle_price_amount")
        elif order_by == "price_down":
            sale_ads = sale_ads.order_by("-vehicle_price_amount")
        elif order_by == "date_at":
            sale_ads = sale_ads.order_by("created_at")
        return sale_ads.all()

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(InventoryGridView, self).get_context_data(**kwargs)
        context['header'] = SettingsHeaderInventoryGrid.objects.last()
        context['footer'] = SettingsFooter.objects.last()
        context['categories'] = CategoriesTrack.objects.all()
        context['models'] = MakeTrack.objects.all()
        context['makes'] = MakeTrack.objects.all()
        context['title'] = 'inventory-grid'
        return context


class InventoryCatalogView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = SaleAds
    template_name = 'inventory-grid.html'
    paginate_by = 24

    def get_queryset(self):
        order_by = self.request.GET.get("order_by")

        qs = super().get_queryset()
        search_title = self.request.GET.get("header-search")
        if search_title:
            qs = qs.filter(title__icontains=search_title)
        category_list = self.request.GET.getlist("category")
        model_list = self.request.GET.getlist("model")
        make_list = self.request.GET.getlist("make")
        try:
            price_min = int(self.request.GET.get("price_min"))
        except (ValueError, TypeError):
            price_min = None
        try:
            price_max = int(self.request.GET.get("price_max"))
        except (ValueError, TypeError):
            price_max = None
        if model_list:
            qs = qs.filter(vehicle_model__id__in=model_list)
        if make_list:
            qs = qs.filter(vehicle_make__id__in=make_list)
        if category_list:
            qs = qs.filter(vehicle_category__id__in=category_list)
        if price_max:
            qs = qs.filter(vehicle_price_amount__lte=price_max)
        if price_min:
            qs = qs.filter(vehicle_price_amount__gte=price_min)
        if order_by == "price_up":
            qs = qs.order_by("vehicle_price_amount")
        elif order_by == "price_down":
            qs = qs.order_by("-vehicle_price_amount")
        elif order_by == "date_at":
            qs = qs.order_by("created_at")

        return qs

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(InventoryCatalogView, self).get_context_data(**kwargs)
        context['header'] = SettingsHeaderInventoryCatalog.objects.last()
        context['footer'] = SettingsFooter.objects.last()
        context['categories'] = CategoriesTrack.objects.all()
        context['models'] = ModelTrack.objects.all()
        context['makes'] = MakeTrack.objects.all()
        context['title'] = 'catalog'
        context['is_catalog'] = True
        return context


class AboutUs(TemplateView):
    template_name = 'about-us.html'

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(AboutUs, self).get_context_data(**kwargs)
        context['header'] = SettingsHeaderAboutUs.objects.last()
        context['footer'] = SettingsFooter.objects.last()
        context['fake_review'] = FakeReviewIndexHome.objects.all()
        context['title'] = 'about us'
        return context


class Privacy(TemplateView):
    template_name = 'privacy.html'

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(Privacy, self).get_context_data(**kwargs)
        context['header'] = SettingsHeaderPrivacy.objects.last()
        context['footer'] = SettingsFooter.objects.last()
        context['title'] = 'privacy'
        return context
