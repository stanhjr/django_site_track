from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView, TemplateView

from site_track.forms import ContactForm
from site_track.models import SaleAds, SettingsFooter, CategoriesTrack, MakeTrack, SettingsIndexHome, \
    SettingsHeaderInventoryGrid, SettingsHeaderInventoryCatalog, SettingsHeaderContact, FakeReviewIndexHome, \
    SettingsHeaderAboutUs, SettingsHeaderPrivacy
from email_sender.tasks import send_mail_contact_us


def main(request):
    return HttpResponse("Hey! It's your main view!!")


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
        return context


class IndexView(ListView):
    model = SaleAds
    template_name = 'index.html'
    paginate_by = 16

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
        return context


class InventoryGridView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = CategoriesTrack
    template_name = 'inventory-grid.html'
    paginate_by = 16

    def get_queryset(self):
        category = self.model.objects.filter(name__iexact=self.kwargs.get("category")).first()
        if category:
            return category.sale_ads.all()
        raise Http404

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(InventoryGridView, self).get_context_data(**kwargs)
        context['header'] = SettingsHeaderInventoryGrid.objects.last()
        context['footer'] = SettingsFooter.objects.last()
        return context


class InventoryCatalogView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = SaleAds
    template_name = 'inventory-grid.html'
    paginate_by = 16

    def get_queryset(self):
        brand = tuple(set(self.request.GET.getlist('brand')))
        if brand:
            brand_qs = self.model.objects.filter(vehicle_model__name__in=brand)
            return brand_qs
        return self.model.objects.all()

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(InventoryCatalogView, self).get_context_data(**kwargs)
        context['header'] = SettingsHeaderInventoryCatalog.objects.last()
        context['footer'] = SettingsFooter.objects.last()
        return context


class AboutUs(TemplateView):
    template_name = 'about-us.html'

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(AboutUs, self).get_context_data(**kwargs)
        context['header'] = SettingsHeaderAboutUs.objects.last()
        context['footer'] = SettingsFooter.objects.last()
        context['fake_review'] = FakeReviewIndexHome.objects.all()
        return context


class Privacy(TemplateView):
    template_name = 'privacy.html'

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(Privacy, self).get_context_data(**kwargs)
        context['header'] = SettingsHeaderPrivacy.objects.last()
        context['footer'] = SettingsFooter.objects.last()
        return context
