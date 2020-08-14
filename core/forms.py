
from django import forms


class StripeForm(forms.Form):
    name = forms.CharField(max_length=50, required=False)
    age = forms.CharField(max_length=50, required=False)
