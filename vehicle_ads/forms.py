from django import forms
from site_track.models import SaleAds, CategoriesTrack, MakeTrack


class DatePickerInput(forms.DateInput):
    input_type = 'date'
    input_formats = ["%Y",]



VEHICLE_WHEEL_DRIVE_CHOICES = (
    ("Front-Wheel-Drive", "Front-Wheel-Drive"),
    ("Four-Wheel-Drive", "Four-Wheel-Drive"),
    ("Rear-Drive", "Rear-Drive")
)

VEHICLE_TRANSMISSION_CHOICES = (
    ("Auto", "Auto"),
    ("Manual", "Manual"),
    ("Semi Auto", "Semi Auto")
)

VEHICLE_WHEEL_CHOICES = (
    ("Left", "Left"),
    ("Right", "Right"),
)

VEHICLE_FUEL_CHOICES = (
    ("Diesel", "Diesel"),
    ("Petrol", "Petrol"),
    ("Electric", "Electric"),
    ("Hybrid", "Hybrid"),
)

VEHICLE_PRICE_TYPE_CHOICES = (
    ("Fixed", "Fixed"),
    ("Negotiable", "Negotiable"),
)

VEHICLE_CONDITION_CHOICES = (
    ("New", "New"),
    ("Used", "Used"),
)


class VehicleInformationForm(forms.ModelForm):
    class Meta:
        model = SaleAds
        fields = '__all__'
        exclude = ('sale_created', 'user')

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(VehicleInformationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field == 'email':
                self.fields[field].initial = self.request.user.email
                self.fields[field].widget = forms.TextInput(attrs={'class': 'form-control', 'type': 'email'})
            elif field == 'phone_number':
                self.fields[field].initial = self.request.user.phone_number
                self.fields[field].widget = forms.TextInput(attrs={'class': 'form-control'})

            elif field == 'preview_image':
                self.fields[field].widget = forms.FileInput(attrs={'class': 'file-input', 'id': 'preview'})

            elif field == "vehicle_category":
                self.fields[field].widget = forms.Select(attrs={'class': 'form-select'},
                                                         choices=CategoriesTrack.get_choices())
            elif field == "vehicle_condition":
                self.fields[field].widget = forms.Select(attrs={'class': 'form-select'},
                                                         choices=VEHICLE_CONDITION_CHOICES)
            elif field == "vehicle_model":
                self.fields[field].widget = forms.Select(attrs={'class': 'form-select'},
                                                         choices=MakeTrack.get_choices())

            elif field == "vehicle_fuel":
                self.fields[field].widget = forms.Select(attrs={'class': 'form-select'},
                                                         choices=VEHICLE_FUEL_CHOICES)

            elif field == "vehicle_year":
                self.fields[field].widget = DatePickerInput(attrs={'class': 'form-control'})
            elif field in ["description", "any_know_problems_with_vehicle"]:
                self.fields[field].widget = forms.Textarea(attrs={'class': 'form-control'})

            elif field in ["tire_percent_front_right", "tire_percent_front_left", "tire_percent_rear_left",
                           "tire_percent_rear_right", "form.tire_percent_rear_drive_tires"]:
                self.fields[field].widget = forms.NumberInput(attrs={'class': 'form-control',
                                                                     'type': 'number', 'min': '1', 'max': '100'})

            else:
                self.fields[field].widget = forms.TextInput(attrs={'class': 'form-control'})


class VehicleInformationUpdateForm(forms.ModelForm):
    class Meta:
        model = SaleAds
        fields = '__all__'
        exclude = ('sale_created', 'user')

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(VehicleInformationUpdateForm, self).__init__(*args, **kwargs)
        initial_data = self.initial
        for field in self.fields:
            self.fields[field].initial = initial_data.get(field)
            if field == 'email':
                self.fields[field].initial = self.request.user.email
                self.fields[field].widget = forms.TextInput(attrs={'class': 'form-control', 'type': 'email'})
            elif field == 'phone_number':
                self.fields[field].initial = self.request.user.phone_number
                self.fields[field].widget = forms.TextInput(attrs={'class': 'form-control'})

            elif field == 'preview_image':
                self.fields[field].widget = forms.FileInput(attrs={'class': 'file-input', 'id': 'preview'})

            elif field == "vehicle_category":
                self.fields[field].widget = forms.Select(attrs={'class': 'form-select'},
                                                         choices=CategoriesTrack.get_choices())
            elif field == "vehicle_model":
                self.fields[field].widget = forms.Select(attrs={'class': 'form-select'},
                                                         choices=MakeTrack.get_choices())

            elif field == "vehicle_fuel":
                self.fields[field].widget = forms.Select(attrs={'class': 'form-select'},
                                                         choices=VEHICLE_FUEL_CHOICES)

            elif field == "vehicle_year":
                self.fields[field].widget = DatePickerInput(attrs={'class': 'form-control'})
            elif field in ["description", "any_know_problems_with_vehicle"]:
                self.fields[field].widget = forms.Textarea(attrs={'class': 'form-control'})

            elif field in ["tire_percent_front_right", "tire_percent_front_left", "tire_percent_rear_left",
                           "tire_percent_rear_right", "form.tire_percent_rear_drive_tires"]:
                self.fields[field].widget = forms.NumberInput(attrs={'class': 'form-control',
                                                                     'type': 'number', 'min': '1', 'max': '100'})

            else:
                self.fields[field].widget = forms.TextInput(attrs={'class': 'form-control'})
