import unittest
from django.test import TestCase
from django.contrib.auth.models import User
from datetime import datetime
from .models import Event, Booking, Payment


class EventModelTestCase(TestCase):
    def setUp(self):
        self.event = Event.objects.create(
            name='Test Event',
            description='This is a test event',
            start_time=datetime.now(),
            end_time=datetime.now(),
            location='Test Location',
            price=100
        )

    def test_event_str(self):
        self.assertEqual(str(self.event), 'Test Event')


class BookingModelTestCase(TestCase):
    def setUp(self):
        self.event = Event.objects.create(name='Test Event', price=100)
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.booking = Booking.objects.create(event=self.event, user=self.user, quantity=2)

    def test_booking_total_amount(self):
        self.assertEqual(self.booking.total_amount, 200)

    def test_booking_str(self):
        self.assertEqual(str(self.booking), '2 tickets for Test Event by testuser')


class PaymentModelTestCase(TestCase):
    def setUp(self):
        self.event = Event.objects.create(name='Test Event', price=100)
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.booking = Booking.objects.create(event=self.event, user=self.user, quantity=1)
        self.payment = Payment.objects.create(booking=self.booking, status='completed')

    def test_payment_str(self):
        self.assertEqual(str(self.payment), 'completed payment for 1 tickets for Test Event by testuser')


if __name__ == '__main__':
    unittest.main()
