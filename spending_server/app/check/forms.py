from django import forms


class FiscalData(forms.Form):
    #field_order = ['fn', 'fd', 'fpd']
    fn = forms.CharField(min_length=16, max_length=16)
    fd = forms.CharField(min_length=5, max_length=6)
    fpd = forms.CharField(min_length=10, max_length=10)