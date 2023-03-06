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

### /admin/
The admin page will let you create data for testing. All data is currently stored in the db.sqlite3 file. 
```
http://localhost:8000/admin/
```
![basic accounts page](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Admin_site/admin_home.png)

### /accounts/
The accounts accesses all the users in the database. you can either return a list of all of them with /accounts or a specific entry with /accounts/1 which will return the first account.
