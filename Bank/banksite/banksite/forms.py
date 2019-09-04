from django import forms
 
class CsvForm(forms.Form):
    csv = forms.FileField()