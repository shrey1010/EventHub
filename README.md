# Event Management Web App
This is an Event Management Web App built using Django Rest Framework (DRF) as the backend and MySQL database. The app provides a platform for users to create, manage, and interact with events. Users can register and log in to their accounts to access various functionalities.

## Functionalities
The Event Management Web App offers the following functionalities:

### User Registration and Login:
 Users can create an account by providing a unique username and password. Registered users can log in to their accounts.

### Token-based Authentication:
 The app uses token-based authentication to protect certain endpoints, ensuring secure access to sensitive operations. Users obtain an access token upon login and include it in subsequent requests to protected endpoints.

### Event Creation: 
Logged-in users can create new events by providing event details such as event name, date, time, location, image, and event type.

### Event Listing:
 Users can view a list of all events available in the system. Events are categorized as global events (visible to all users) and user-specific events (visible only to the creator).

### Event Details:
 Users can view the details of a specific event, including event name, date, time, location, image, event type, and the number of likes.

### Event Update and Deletion: 
Users can update the details of an event they have created. They can also delete events they have created.

### Event Likes:
 Users can like and unlike events. The number of likes for each event is displayed in the event details.

### User-specific Events: 
Registered users can view events that match their tag preferences. They can save their tag preferences to filter events based on their interests.

### Filter Events: 
Users can filter events based on different parameters, such as date and time. This feature allows users to find events based on specific criteria.

### Search Events:
 Users can search for events based on keywords. The search functionality enables users to quickly find events of interest.

### Event Tags: 
Events can have multiple tags associated with them. Tags are used to categorize events and enable filtering and searching based on tags.

### Tag Listing: 
Users can view all available tags in the system.

## How to Use
### Prerequisites
Python 3.7 or higher
MySQL database
## Installation
### Clone the repository:
git clone https://github.com/shrey1010/event-management-webapp.git
cd event-management-webapp
### Install required packages:

### Set up MySQL database:

Create a new database in MySQL and update the database settings in eventapp/settings.py.
### Apply migrations:

python manage.py makemigrations
python manage.py migrate
Create a superuser:

python manage.py createsuperuser
### Run the development server:

python manage.py runserver
Access the app at http://localhost:8000/.

## API Endpoints
api/events/: View and create events (requires authentication).

api/events/<event_id>/: Retrieve, update, and delete a specific event (requires authentication).

api/events/<event_id>/like/: Like or unlike an event (requires authentication).

api/events/<event_id>/register/: Register for an event (requires authentication).

api/tags/: View all available tags.

## Authentication
Token-based authentication is used in this app. To access protected endpoints, users need to obtain an access token by logging in. The access token should be included in the headers of subsequent requests to protected endpoints.

To obtain a token, make a POST request to http://localhost:8000/api/token/ with the user's credentials (username and password). The response will contain an access token, which should be included in the headers for subsequent requests.

## Credits
This project was developed by Shrey.

## Feedback and Contributions
Feedback and contributions are welcome! If you have any suggestions or find any issues, please create an issue or submit a pull request.

