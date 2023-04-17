from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['num_tickets']
        labels = {'num_tickets': 'Number of tickets'}
