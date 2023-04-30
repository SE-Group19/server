from django import forms
from .models import Booking

# This is designed to be used to render a form to
# create or update a Booking object in the database.


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['num_tickets']
        labels = {'num_tickets': 'Number of tickets'}
