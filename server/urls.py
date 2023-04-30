from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.say_hello),
    path('home/', views.home),
    path('event_detail/<int:event_id>/', views.event_detail, name='event_detail'),
    path('book_event/<int:event_id>/book/', views.book_event, name='book_event'),
    path('my_bookings/', views.my_bookings, name='my_bookings'),
    ]