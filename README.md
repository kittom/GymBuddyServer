# GymBuddy
A computer vision and social media fitness app, for checking the quality of exercises and sharing with your friends.

## Setup
create a venv. 
```
python3 -m venv /path/to/new/virtual/environment
```
Select this interpreter and install django, and the django rest framework.
```
pip install django
pip install djangorestframework
```

With these installed, run the server through the manage.py file.
```
python manage.py runserver
```
the server will be running on localhost:8000

## API

The API has all of the models for the GymBuddy App, as described in the design document.
The current features include, CRUD functions for each model, however, there is no logic between components.
