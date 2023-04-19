# GymBuddy

A computer vision and social media fitness app, for checking the quality of exercises and sharing with your friends.

## Setup

Create a new virtual environment.

```bash
python -m venv venv
```

Activate your new virtual environment
On Mac and linux:
```bash
source venv/bin/activate
```

install the packages
```bash
pip install -r requirements.txt
```

update the settings.py in the gym 

Select this interpreter and install django, and the django rest framework.

```bash
pip install django
pip install djangorestframework
```

With these installed, run the server through the manage.py file.

```bash
python manage.py runserver
```

the server will be running on localhost:8000

![basic accounts page](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Admin_site/admin_home.png)

### /accounts/

The accounts accesses all the users in the database. you can either return a list of all of them with /accounts or a specific entry with /accounts/1 which will return the first account.
