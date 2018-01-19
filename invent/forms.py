from django import forms
from .models import Units, DeliveryAddress, Customer
class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
class InventoryPart(forms.Form):
    part_no = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Part no'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Description'}))
    notes = forms.CharField(required=False,widget=forms.Textarea(attrs={'class':'form-control form-control-sm','placeholder':'Notes'}))
    unit = forms.CharField(required=True, widget=forms.Select(choices=Units.objects.all().values_list('id','code'),attrs={'class':'form-control form-control-sm','placeholder':'Unit'}))
    active = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'form-control form-control-sm','placeholder':'Active'}))
class CustomerForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Name'}))
    vat_no = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'VAT no'}))
    address1 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Address line 1'}))
    address2 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Address line 2'}),required=False)
    phone1 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Phone 1'}))
    phone2 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Phone 2'}),required=False)
    email= forms.CharField(widget=forms.TextInput(attrs={'type':'email','class':'form-control form-control-sm','placeholder':'e-mail'}),required=False)
    notes = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control form-control-sm','placeholder':'Notes'}),required=False)
class DeliveryAddressForm(forms.Form):
    customer = forms.CharField(widget=forms.Select(choices=Customer.objects.all().values_list('id', 'name'),attrs={'class':'form-control form-control-sm','placeholder':'Customer'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Description'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control form-control-sm','placeholder':'Address'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Phone'}),required=False)
    email = forms.CharField(widget=forms.TextInput(attrs={'type':'email','class':'form-control form-control-sm','placeholder':'e-mail'}),required=False)