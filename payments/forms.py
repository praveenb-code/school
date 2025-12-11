from django import forms
from .models import Payment

class PaymentForm(forms.ModelForm):
    student_id = forms.CharField(required=True, label='Student ID')

    class Meta:
        model = Payment
        fields = ['payment_type', 'amount', 'method', 'note']
