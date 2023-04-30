# Event Booking System

This is a Django backend application for an event booking system with RESTful API using Django REST framework. It allows users to create events, make bookings, and process payments.

## Features

-   List all events
-   Create a new event
-   Retrieve a specific event
-   Update a specific event
-   Delete a specific event
-   List all bookings
-   Create a new booking
-   Retrieve a specific booking
-   Update a specific booking
-   Delete a specific booking
-   Token-based authentication
-   Payment processing

## Technologies

-   Python
-   Django
-   Django REST framework

## Setup

1. Clone the repository
2. Create a virtual environment and activate it
3. Install the dependencies
4. Create a database
5. Run the server
6. Access the API

## File Structure

The folder structure of the project is as follows:

-   `server/` - The root directory of the project.
    -   `core/` - Configuration directory.
        -   `asgi.py` -
        -   `settings.py` - Contains the project settings.
        -   `urls.py` - Contains the URL routes of the project.
        -   `wsgi.py` - Contains the WSGI application.
    -   `server/` - The main application directory.
        -   `migrations/` - Database migration files.
        -   `templates/` - HTML templates.
        -   `admin.py` - contains the admin priviledges of the app
        -   `app` -
        -   `tests/` - Test files.
        -   `models.py` - Contains the models of the app.
        -   `serializers.py` - Contains the serializers of the app.
        -   `urls.py` - Contains the URL routes of the app.
        -   `views.py` - Contains the views of the app.
    -   `.gitignore` - Prevents the .venv folder, other folders and files which are not needed to be pushed to github.
    -   `manage.py` - starts development server
    -   `requirements.txt` - A file containing all the required Python packages and their versions.
    -   `README.md` - Contains the documentation of the project.

## API Endpoints

-   `GET /api/events/` - List all events
-   `POST /api/events/` - Create a new event
-   `GET /api/events/:id/` - Retrieve a specific event
-   `PUT /api/events/:id/` - Update a specific event
-   `DELETE /api/events/:id/` - Delete a specific event
-   `GET /api/bookings/` - List all bookings
-   `POST /api/bookings/` - Create a new booking
-   `GET /api/bookings/:id/` - Retrieve a specific booking
-   `PUT /api/bookings/:id/` - Update a specific booking
-   `DELETE /api/bookings/:id/` - Delete a specific booking
-   `POST /api-token-auth/` - Token-based authentication

## Authentication

The API requires token-based authentication to make bookings. To authenticate, send a `POST` request to `/api-token-auth/` with the `username` and `password` fields in the request body. The response will include an `access_token` field that you can use in subsequent requests.

## Payment

The application allows users to process payments. When a booking is made, the payment status is set to `pending`. After the payment is processed, the payment status is updated to either `complete` or `fail`.

## Conclusion

This Django backend application provides a simple event booking system with RESTful API using Django REST framework. It can be extended further to add more features like user authentication, email notifications, and more.
