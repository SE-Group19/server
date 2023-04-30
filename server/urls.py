from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from .views import event_list, event_detail, booking_list, booking_detail

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('api/events/', event_list, name='event_list'),
    path('api/events/<int:pk>/', event_detail, name='event_detail'),
    path('api/bookings/', booking_list, name='booking_list'),
    path('api/bookings/<int:pk>/', booking_detail, name='booking_detail'),
]