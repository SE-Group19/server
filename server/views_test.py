import unittest
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Booking, Event
from .serializers import BookingSerializer, EventSerializer


# initialize the APIClient app
client = APIClient()


class EventTestCase(TestCase):
    def setUp(self):
        self.event1 = Event.objects.create(
            name='Event 1',
            date='2023-05-01',
            description='This is event 1'
        )
        self.event2 = Event.objects.create(
            name='Event 2',
            date='2023-05-02',
            description='This is event 2'
        )

        self.valid_payload = {
            'name': 'Test Event',
            'date': '2023-05-03',
            'description': 'This is a test event'
        }
        self.invalid_payload = {
            'name': '',
            'date': '',
            'description': ''
        }

    def test_get_all_events(self):
        # get API response
        response = client.get(reverse('event-list'))
        # get data from db
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_valid_event(self):
        response = client.post(
            reverse('event-list'),
            data=self.valid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_event(self):
        response = client.post(
            reverse('event-list'),
            data=self.invalid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_valid_event(self):
        response = client.get(reverse('event-detail', kwargs={'pk': self.event1.pk}))
        event = Event.objects.get(pk=self.event1.pk)
        serializer = EventSerializer(event)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_event(self):
        response = client.get(reverse('event-detail', kwargs={'pk': 100}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_valid_event(self):
        response = client.put(
            reverse('event-detail', kwargs={'pk': self.event1.pk}),
            data=self.valid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_invalid_event(self):
        response = client.put(
            reverse('event-detail', kwargs={'pk': self.event1.pk}),
            data=self.invalid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_valid_event(self):
        response = client.delete(reverse('event-detail', kwargs={'pk': self.event1.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_invalid_event(self):
        response = client.delete(reverse('event-detail', kwargs={'pk': 100}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class BookingTestCase(TestCase):
    def setUp(self):
        self.event1 = Event.objects.create(
            name='Event 1',
            date='2023-05-01',
            description='This is event 1'
        )
        self.booking1 = Booking.objects.create(
            event=self.event1,
            name='Test Booking 1',
            email='test1@example.com'

        )


if __name__ == '__main__':
    unittest.main()
