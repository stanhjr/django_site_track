from django import forms
from django.forms.models import model_to_dict
from site_track.models import SaleAds


VEHICLE_TYPE_CHOICES = (
            ("Wagon", "Wagon"),
            ("Hatchback", "Hatchback"),
            ("Convertible", "Convertible")
        )

VEHICLE_FUEL_CHOICES = (
            ("Diesel", "Diesel"),
            ("Petrol", "Petrol"),
            ("Electric", "Electric"),
            ("Hybrid", "Hybrid"),
        )

VEHICLE_PRICE_TYPE_CHOICES = (
            ("Fixed", "Diesel"),
            ("Negotiable", "Petrol"),
        )

VEHICLE_CONDITION_CHOICES = (
            ("New", "New"),
            ("Used", "Used"),
        )


class VehicleInformationForm(forms.ModelForm):
    class Meta:
        model = SaleAds
        fields = '__all__'

    def __init__(self, *args, **kwargs):

        self.request = kwargs.pop('request', None)
        super(VehicleInformationForm, self).__init__(*args, **kwargs)
        sale_created = self.request.user.get_sale_created()
        self.sale_dict = {}
        if sale_created:
            print(222222222222222222)
            self.sale_dict = model_to_dict(sale_created)
        for field in self.fields:
            self.fields[field].initial = self.sale_dict.get(field)
            if field == "vehicle_type":
                self.fields[field].widget = forms.Select(attrs={'class': 'form-select'},
                                                         choices=VEHICLE_TYPE_CHOICES)
            elif field == "vehicle_fuel":
                self.fields[field].widget = forms.Select(attrs={'class': 'form-select'},
                                                         choices=VEHICLE_FUEL_CHOICES)
            elif field == "vehicle_price_type":
                self.fields[field].widget = forms.Select(attrs={'class': 'form-select'},
                                                         choices=VEHICLE_PRICE_TYPE_CHOICES)
            elif field == "vehicle_condition":
                self.fields[field].widget = forms.Select(attrs={'class': 'form-select'},
                                                         choices=VEHICLE_CONDITION_CHOICES)
            elif field in ["date_of_issue", "date_of_expire", "vehicle_year"]:
                self.fields[field].widget = forms.SelectDateWidget(attrs={'class': 'form-control'})
            elif field == "description":
                self.fields[field].widget = forms.TextInput(attrs={'class': 'form-control'})

            else:
                self.fields[field].widget = forms.TextInput(attrs={'class': 'form-control'})