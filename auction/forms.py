from django import forms
from site_track.models import SaleAds


class AuctionBetForm(forms.ModelForm):
    class Meta:
        model = SaleAds
        fields = ('last_price',)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(AuctionBetForm, self).__init__(*args, **kwargs)
        self.fields['last_price'].widget = forms.TextInput(attrs={'class': 'form-control', 'type': 'text'})


