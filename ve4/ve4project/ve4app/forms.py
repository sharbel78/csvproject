from django import forms
from .models import CSVfile

class csvFileform(forms.ModelForm):
    class Meta:
        model = CSVfile
        fields =['file']