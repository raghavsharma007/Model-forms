from django import forms
from .models import FillDetails


class FormFill(forms.ModelForm):
    class Meta:
        model = FillDetails
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type':'date'})
        }