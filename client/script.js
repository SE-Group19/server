const apiUrl = "http://localhost:8000/events/";

// Get events from the API
fetch(apiUrl)
    .then((response) => response.json())
    .then((events) => {
        // Create a list of events
        const eventList = document.getElementById("event-list");
        events.forEach((event) => {
            const li = document.createElement("li");
            li.textContent = `${event.name} - ${event.date}`;
            li.addEventListener("click", () => {
                // Redirect the user to the event booking page with the selected event ID
                window.location.href = `booking.html?event_id=${event.id}`;
            });
            eventList.appendChild(li);
        });
    })
    .catch((error) => console.error(error));
