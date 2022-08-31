from django import forms
from site_track.models import SaleAds, CategoriesTrack, MakeTrack, MyUser, ModelTrack, ShouldInclude, TruckModel, \
    TruckMake, TypeOfTrailer, SpringRide


class DatePickerInput(forms.DateInput):
    input_type = 'date'


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

# category_truck = CategoriesTrack.objects.filter(name='Truck').first()
# category_trailer = CategoriesTrack.objects.filter(name='Trailer').first()
category_truck = 2
category_trailer = 4


class BaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        for bound_field in self:
            if hasattr(bound_field, "field") and bound_field.field.required:
                bound_field.field.widget.attrs["required"] = "required"

class VehicleInformationForm(BaseForm):
    class Meta:
        model = SaleAds
        fields = '__all__'
        exclude = ('sale_created', 'user', 'user_bet', 'user_watch', 'sales', 'last_price')

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(VehicleInformationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = False

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
                self.fields[field].initial = category_trailer
            elif field == "vehicle_condition":
                self.fields[field].widget = forms.Select(attrs={'class': 'form-select'},
                                                         choices=VEHICLE_CONDITION_CHOICES)
            elif field == "vehicle_model":
                self.fields[field].widget = forms.Select(attrs={'class': 'form-select'},
                                                         choices=ModelTrack.get_choices())
            elif field == "vehicle_make":
                self.fields[field].widget = forms.Select(attrs={'class': 'form-select'},
                                                         choices=MakeTrack.get_choices())

            elif field == "vehicle_fuel":
                self.fields[field].widget = forms.Select(attrs={'class': 'form-select'},
                                                         choices=VEHICLE_FUEL_CHOICES)

            elif field in ["vehicle_year", "sale_end_time"]:
                self.fields[field].widget = DatePickerInput(attrs={'class': 'form-control'})
            elif field in ["description", "any_know_problems_with_vehicle"]:
                self.fields[field].widget = forms.Textarea(attrs={'class': 'form-control'})

            elif field in ["tire_percent_front_right", "tire_percent_front_left", "tire_percent_rear_left",
                           "tire_percent_rear_right", "form.tire_percent_rear_drive_tires"]:
                self.fields[field].widget = forms.NumberInput(attrs={'class': 'form-control',
                                                                     'type': 'number', 'min': '1', 'max': '100'})

            else:
                self.fields[field].widget = forms.TextInput(attrs={'class': 'form-control'})



class TruckCreateForm(BaseForm):
    class Meta:
        model = SaleAds
        fields = '__all__'
        exclude = ('sale_created', 'user', 'user_bet', 'user_watch', 'sales', 'last_price')

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(TruckCreateForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = False
            if field == 'vehicle_mileage':
                self.fields[field].initial = ''
            if field == 'email':
                self.fields[field].initial = self.request.user.email
                self.fields[field].widget = forms.TextInput(attrs={'class': 'form-control', 'type': 'email'})
            elif field == 'phone_number':
                self.fields[field].initial = self.request.user.phone_number
                self.fields[field].widget = forms.TextInput(attrs={'class': 'form-control'})

            elif field == 'preview_image':
                self.fields[field].widget = forms.FileInput(attrs={'class': 'file-input', 'id': 'preview'})

            elif field == "vehicle_condition":
                self.fields[field].widget = forms.Select(attrs={'class': 'form-select'},
                                                         choices=VEHICLE_CONDITION_CHOICES)

            elif field == "should_include":
                self.fields[field].widget = forms.Select(attrs={'class': 'form-select'},
                                                         choices=ShouldInclude.get_choices())
            elif field == "truck_model":
                self.fields[field].widget = forms.Select(attrs={'class': 'form-select'},
                                                         choices=TruckModel.get_choices())
            elif field == "truck_make":
                self.fields[field].widget = forms.Select(attrs={'class': 'form-select'},
                                                         choices=TruckMake.get_choices())
            elif field == 'type_of_5_trailer':
                self.fields[field].widget = forms.Select(attrs={'class': 'form-select'},
                                                         choices=TypeOfTrailer.get_choices())
            elif field == 'spring_ride':
                self.fields[field].widget = forms.Select(attrs={'class': 'form-select'},
                                                         choices=SpringRide.get_choices())

            elif field in ["vehicle_year", "sale_end_time"]:
                self.fields[field].widget = DatePickerInput(attrs={'class': 'form-control'})
            elif field in ["description", "any_know_problems_with_vehicle"]:
                self.fields[field].widget = forms.Textarea(attrs={'class': 'form-control'})

            elif field in ["tire_percent_front_right", "tire_percent_front_left", "tire_percent_rear_left",
                           "tire_percent_rear_right", "form.tire_percent_rear_drive_tires"]:
                self.fields[field].widget = forms.NumberInput(attrs={'class': 'form-control',
                                                                     'type': 'number', 'min': '1', 'max': '100'})
            elif field == "vehicle_category":
                self.fields[field].initial = category_truck

            else:
                self.fields[field].widget = forms.TextInput(attrs={'class': 'form-control'})


class TruckUpdateForm(BaseForm):
    class Meta:
        model = SaleAds
        fields = '__all__'
        exclude = ('sale_created', 'user', 'user_bet', 'user_watch', 'sales', 'last_price')

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(TruckUpdateForm, self).__init__(*args, **kwargs)
        initial_data = self.initial
        for field in self.fields:
            self.fields[field].initial = initial_data.get(field)
            if field == 'vehicle_mileage':
                self.fields[field].initial = ''
            if field == 'email':
                self.fields[field].initial = self.request.user.email
                self.fields[field].widget = forms.TextInput(attrs={'class': 'form-control', 'type': 'email'})
            elif field == 'phone_number':
                self.fields[field].initial = self.request.user.phone_number
                self.fields[field].widget = forms.TextInput(attrs={'class': 'form-control'})

            elif field == 'preview_image':
                self.fields[field].widget = forms.FileInput(attrs={'class': 'file-input', 'id': 'preview'})

            elif field == "vehicle_condition":
                self.fields[field].widget = forms.Select(attrs={'class': 'form-select'},
                                                         choices=VEHICLE_CONDITION_CHOICES)

            elif field == "should_include":
                self.fields[field].widget = forms.Select(attrs={'class': 'form-select'},
                                                         choices=ShouldInclude.get_choices())
            elif field == "truck_model":
                self.fields[field].widget = forms.Select(attrs={'class': 'form-select'},
                                                         choices=TruckModel.get_choices())
            elif field == "truck_make":
                self.fields[field].widget = forms.Select(attrs={'class': 'form-select'},
                                                         choices=TruckMake.get_choices())
            elif field == 'type_of_5_trailer':
                self.fields[field].widget = forms.Select(attrs={'class': 'form-select'},
                                                         choices=TypeOfTrailer.get_choices())
            elif field == 'spring_ride':
                self.fields[field].widget = forms.Select(attrs={'class': 'form-select'},
                                                         choices=SpringRide.get_choices())

            elif field in ["vehicle_year", "sale_end_time"]:
                self.fields[field].widget = DatePickerInput(attrs={'class': 'form-control'})
            elif field in ["description", "any_know_problems_with_vehicle"]:
                self.fields[field].widget = forms.Textarea(attrs={'class': 'form-control'})

            elif field in ["tire_percent_front_right", "tire_percent_front_left", "tire_percent_rear_left",
                           "tire_percent_rear_right", "form.tire_percent_rear_drive_tires"]:
                self.fields[field].widget = forms.NumberInput(attrs={'class': 'form-control',
                                                                     'type': 'number', 'min': '1', 'max': '100'})

            else:
                self.fields[field].widget = forms.TextInput(attrs={'class': 'form-control'})


class VehicleInformationUpdateForm(BaseForm):
    class Meta:
        model = SaleAds
        fields = '__all__'
        exclude = ('sale_created', 'user', 'user_bet', 'user_watch', 'sales', 'last_price')

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(VehicleInformationUpdateForm, self).__init__(*args, **kwargs)
        initial_data = self.initial
        for field in self.fields:
            self.fields[field].initial = initial_data.get(field)
            if field == 'vehicle_mileage':
                self.fields[field].initial = ''
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
                                                         choices=ModelTrack.get_choices())
            elif field == "vehicle_make":
                self.fields[field].widget = forms.Select(attrs={'class': 'form-select'},
                                                         choices=MakeTrack.get_choices())

            elif field == "vehicle_fuel":
                self.fields[field].widget = forms.Select(attrs={'class': 'form-select'},
                                                         choices=VEHICLE_FUEL_CHOICES)

            elif field in ["vehicle_year", "sale_end_time"]:
                self.fields[field].widget = DatePickerInput(attrs={'class': 'form-control'})
            elif field in ["description", "any_know_problems_with_vehicle"]:
                self.fields[field].widget = forms.Textarea(attrs={'class': 'form-control'})

            elif field in ["tire_percent_front_right", "tire_percent_front_left", "tire_percent_rear_left",
                           "tire_percent_rear_right", "form.tire_percent_rear_drive_tires"]:
                self.fields[field].widget = forms.NumberInput(attrs={'class': 'form-control',
                                                                     'type': 'number', 'min': '1', 'max': '100'})

            else:
                self.fields[field].widget = forms.TextInput(attrs={'class': 'form-control'})


class SendEmailVendorForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['email', 'first_name', 'phone_number']

    enter_your_offer_price = forms.CharField()
    describe_your_message = forms.CharField()

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(SendEmailVendorForm, self).__init__(*args, **kwargs)
        initial_data = self.initial
        for field in self.fields:
            self.fields[field].initial = initial_data.get(field)
            if field == 'email':
                self.fields[field].initial = self.request.user.email
                self.fields[field].widget = forms.TextInput(attrs={'class': 'form-control', 'type': 'email'})
            elif field == 'first_name':
                self.fields[field].initial = self.request.user.first_name
                self.fields[field].widget = forms.TextInput(attrs={'class': 'form-control'})
            elif field == 'phone_number':
                self.fields[field].initial = self.request.user.phone_number
                self.fields[field].widget = forms.TextInput(attrs={'class': 'form-control'})

            elif field == 'enter_your_offer_price':
                self.fields[field].widget = forms.NumberInput(attrs={'class': 'form-control',
                                                                     'type': 'number', 'min': '1'})

            else:
                self.fields[field].widget = forms.Textarea(attrs={'class': 'form-control'})
