from django import forms
from site_track.models import SaleAds, CategoriesTrack, MakeTrack, MyUser, ModelTrack, TypeOfTruck, TruckModel, \
    TruckMake, TypeOfTrailer, SizeOfTrailer, Suspension, SleeperSize, Transmission, Horsepower, Engine, TypeOf5Wheel, \
    TireSize


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
    ("LPG", "LPG"),
)

VEHICLE_PRICE_TYPE_CHOICES = (
    ("Fixed", "Fixed"),
    ("Negotiable", "Negotiable"),
)

VEHICLE_CONDITION_CHOICES = (
    ("New", "New"),
    ("Used", "Used"),
)
JAKE_BRAKE_CHOICES = (
    ("Yes", "Yes"),
    ("No", "No"),
)

category_truck = CategoriesTrack.objects.filter(name='Truck').first()
category_trailer = CategoriesTrack.objects.filter(name='Trailer').first()


class BaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        for bound_field in self:
            if hasattr(bound_field, "field") and bound_field.field.required:
                bound_field.field.widget.attrs["required"] = "required"


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
            elif field == "jake_brake":
                self.fields[field].widget = forms.Select(attrs={'class': 'form-select'},
                                                        choices=JAKE_BRAKE_CHOICES)

            elif field == "type_of_truck":
                self.fields[field].widget = forms.Select(attrs={'class': 'form-select'},
                                                         choices=TypeOfTruck.get_choices())
            elif field == "sleeper_size":
                self.fields[field].widget = forms.Select(attrs={'class': 'form-select'},
                                                         choices=SleeperSize.get_choices())
            elif field == "engine":
                self.fields[field].widget = forms.Select(attrs={'class': 'form-select'},
                                                         choices=Engine.get_choices())
            elif field == "horse_power":
                self.fields[field].widget = forms.Select(attrs={'class': 'form-select'},
                                                         choices=Horsepower.get_choices())
            elif field == "transmission":
                self.fields[field].widget = forms.Select(attrs={'class': 'form-select'},
                                                         choices=Transmission.get_choices())
            elif field == "tire_size":
                self.fields[field].widget = forms.Select(attrs={'class': 'form-select'},
                                                         choices=TireSize.get_choices())
            elif field == "type_of_5_wheel":
                self.fields[field].widget = forms.Select(attrs={'class': 'form-select'},
                                                         choices=TypeOf5Wheel.get_choices())

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


class TrailerCreateForm(BaseForm):
    class Meta:
        model = SaleAds
        fields = '__all__'
        exclude = ('sale_created', 'user', 'user_bet', 'user_watch', 'sales', 'last_price')

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(TrailerCreateForm, self).__init__(*args, **kwargs)
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

            elif field == "truck_model":
                self.fields[field].widget = forms.Select(attrs={'class': 'form-select'},
                                                         choices=TruckModel.get_choices())
            elif field == "truck_make":
                self.fields[field].widget = forms.Select(attrs={'class': 'form-select'},
                                                         choices=TruckMake.get_choices())
            elif field == 'type_of_5_trailer':
                self.fields[field].widget = forms.Select(attrs={'class': 'form-select'},
                                                         choices=TypeOfTrailer.get_choices())
            elif field == 'size_of_trailer':
                self.fields[field].widget = forms.Select(attrs={'class': 'form-select'},
                                                         choices=SizeOfTrailer.get_choices())
            elif field == 'suspension':
                self.fields[field].widget = forms.Select(attrs={'class': 'form-select'},
                                                         choices=Suspension.get_choices())
            elif field == "tire_size":
                self.fields[field].widget = forms.Select(attrs={'class': 'form-select'},
                                                         choices=TireSize.get_choices())

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


class TrailerUpdateForm(BaseForm):
    class Meta:
        model = SaleAds
        fields = '__all__'
        exclude = ('sale_created', 'user', 'user_bet', 'user_watch', 'sales', 'last_price')

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(TrailerUpdateForm, self).__init__(*args, **kwargs)
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

            elif field == "truck_model":
                self.fields[field].widget = forms.Select(attrs={'class': 'form-select'},
                                                         choices=TruckModel.get_choices())
            elif field == "truck_make":
                self.fields[field].widget = forms.Select(attrs={'class': 'form-select'},
                                                         choices=TruckMake.get_choices())
            elif field == 'type_of_5_trailer':
                self.fields[field].widget = forms.Select(attrs={'class': 'form-select'},
                                                         choices=TypeOfTrailer.get_choices())
            elif field == 'size_of_trailer':
                self.fields[field].widget = forms.Select(attrs={'class': 'form-select'},
                                                         choices=SizeOfTrailer.get_choices())
            elif field == 'suspension':
                self.fields[field].widget = forms.Select(attrs={'class': 'form-select'},
                                                         choices=Suspension.get_choices())
            elif field == "tire_size":
                self.fields[field].widget = forms.Select(attrs={'class': 'form-select'},
                                                         choices=TireSize.get_choices())

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

            elif field == "vehicle_category":
                self.fields[field].widget = forms.Select(attrs={'class': 'form-select'},
                                                         choices=CategoriesTrack.get_choices())

            elif field == "type_of_truck":
                self.fields[field].widget = forms.Select(attrs={'class': 'form-select'},
                                                         choices=TypeOfTruck.get_choices())

            elif field == "sleeper_size":
                self.fields[field].widget = forms.Select(attrs={'class': 'form-select'},
                                                         choices=SleeperSize.get_choices())
            elif field == "engine":
                self.fields[field].widget = forms.Select(attrs={'class': 'form-select'},
                                                         choices=Engine.get_choices())
            elif field == "horse_power":
                self.fields[field].widget = forms.Select(attrs={'class': 'form-select'},
                                                         choices=Horsepower.get_choices())
            elif field == "transmission":
                self.fields[field].widget = forms.Select(attrs={'class': 'form-select'},
                                                         choices=Transmission.get_choices())
            elif field == "type_of_5_wheel":
                self.fields[field].widget = forms.Select(attrs={'class': 'form-select'},
                                                         choices=TypeOf5Wheel.get_choices())
            elif field == "jake_brake":
                self.fields[field].widget = forms.Select(attrs={'class': 'form-select'},
                                                         choices=JAKE_BRAKE_CHOICES)

            elif field == "vehicle_condition":
                self.fields[field].widget = forms.Select(attrs={'class': 'form-select'},
                                                         choices=VEHICLE_CONDITION_CHOICES)
            elif field == "vehicle_model":
                self.fields[field].widget = forms.Select(attrs={'class': 'form-select'},
                                                         choices=ModelTrack.get_choices())
            elif field == "vehicle_make":
                self.fields[field].widget = forms.Select(attrs={'class': 'form-select'},
                                                         choices=MakeTrack.get_choices())
            elif field == "tire_size":
                self.fields[field].widget = forms.Select(attrs={'class': 'form-select'},
                                                         choices=TireSize.get_choices())

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
