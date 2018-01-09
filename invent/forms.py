from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
class InventoryPart(forms.Form):
    part_no = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Part no'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Description'}))
    notes = forms.CharField(required=False,widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Notes'}))
    #unit = forms.ForeignKey('Units')
   # active = forms.BooleanField(required=False)
