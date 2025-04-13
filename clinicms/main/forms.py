from django import forms
from .models import Patient, Prescription,Billing

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ['patient', 'diagnosis', 'medicines']
from .models import Billing



class BillingForm(forms.ModelForm):
    class Meta:
        model = Billing
        fields = ['patient', 'services', 'total_amount']
        widgets = {
            'services': forms.Textarea(attrs={'rows': 3}),
        }
