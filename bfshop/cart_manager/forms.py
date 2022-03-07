from django import forms

a = [(i, str(i)) for i in range(1, 21)]

class CartAddProductForm(forms.Form):
    county = forms.TypedChoiceField(choices = a, coerce = int)
    update = forms.BooleanField(required = False, initial = False, widget = forms.HiddenInput)