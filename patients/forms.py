from django import forms
from .models import patient


class PatientForm(forms.ModelForm):
    class Meta:
        model = patient
        fields = ['name', 'phone', 'email']