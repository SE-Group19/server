from django.shortcuts import render, redirect , get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import Event, Booking
from .forms import BookingForm
from django.template import loader


def say_hello(request):
    return HttpResponse('Hello world')


def home(request):
    events = Event.objects.all()
    return render(request, 'server/home.html', {'events': events})


def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    template = loader.get_template('event.html')
    return HttpResponse(render(request, 'server/event_detail.html', {'event': event}))
    #return render(request, 'server/event_detail.html', {'event': event})


def book_event(request, event_id):
    template = loader.get_template('event.html')
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.event = event
            booking.save()
            messages.success(request, 'Booking successful!')
            return redirect('my_bookings')
    else:
        form = BookingForm()
    return render(request, 'server/book_event.html', {'event': event, 'form': form})


def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    template = loader.get_template('event.html')
    return render(request, 'server/my_bookings.html', {'bookings': bookings})
