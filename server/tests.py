from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Event
from .serializers import EventSerializer


class EventListTests(APITestCase):
    def test_list_events(self):
        url = reverse('event-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        self.assertEqual(response.data, serializer.data)

    def test_create_event(self):
        url = reverse('event-list')
        data = {'name': 'Test Event', 'date': '2023-05-01', 'location': 'Test Location'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        event = Event.objects.get(pk=response.data['id'])
        self.assertEqual(event.name, data['name'])
        self.assertEqual(event.date, data['date'])
        self.assertEqual(event.location, data['location'])