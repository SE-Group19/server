from rest_framework import serializers
from .models import Event, Booking, Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('id', 'booking', 'status', 'created_at', 'updated_at')


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'name', 'description', 'start_time', 'end_time', 'location', 'price')


class BookingSerializer(serializers.ModelSerializer):
    payments = PaymentSerializer(many=True, read_only=True)

    class Meta:
        model = Booking
        fields = ('id', 'event', 'user', 'quantity', 'total_amount', 'payments')
        read_only_fields = ('total_amount',)
