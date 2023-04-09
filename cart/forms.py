from django import forms

Laptop_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddLaptopForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=Laptop_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)