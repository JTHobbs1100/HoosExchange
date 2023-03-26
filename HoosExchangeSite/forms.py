from django import forms
from django.forms import ModelForm
from HoosExchangeSite.models import Listing
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile

TYPES = (
    ("Bottoms", "Bottoms"),
    ("Top", "Top"),
    ("Shoes", "Shoes"),
    ("Accessory", "Accessory"),
)
class makeListingForm(ModelForm):
    #Name, tag type, picture of item, price (if any), contact info (email/phone), description
    # term = forms.ChoiceField(choices=TERMCHOICES)
    # subject = forms.CharField(label='subject', max_length=100, required=False)
    # catalog_nbr = forms.IntegerField(required=False)
    # page = forms.IntegerField(max_value=100, initial=1)

    # name = forms.CharField(label='name', max_length=100, required=True)
    # tag = forms.ChoiceField(choices=TYPES) #change to types
    # description = forms.CharField(max_length=1000)
    # price = forms.DecimalField(decimal_places=2, max_digits=10)
    # phone_number = forms.IntegerField(max_value=9999999999)
    # email = forms.CharField(max_length=100)
    # img = forms.ImageField()

    class Meta:
        model = Listing
        fields = ['person_name', 'tag', 'description', 'price', 'phone_number', 'email', 'image','item_name'] #add image here







