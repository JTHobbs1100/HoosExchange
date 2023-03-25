from django import forms

TYPES = (
    ("Bottoms"),
    ("Top"),
    ("Shoes"),
    ("Accessory"),
)
class makeListingForm(forms.Form):
    #Name, tag type, picture of item, price (if any), contact info (email/phone), description
    # term = forms.ChoiceField(choices=TERMCHOICES)
    # subject = forms.CharField(label='subject', max_length=100, required=False)
    # catalog_nbr = forms.IntegerField(required=False)
    # page = forms.IntegerField(max_value=100, initial=1)

    name = forms.CharField(label='name', max_length=100, required=True)
    tag = forms.ChoiceField(choices=TYPES)
    


