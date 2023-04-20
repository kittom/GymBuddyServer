# GymBuddy

A computer vision and social media fitness app, for checking the quality of exercises and sharing with your friends.

## Setup

First, make sure you have Python installed on your machine.

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

update the current_ip in the settings.py file located in the GymBuddyServer/GymBuddyServer/ directory to include your current IP Address.

```python
current_ip = "" # insert current ip address
```


With these installed, run the server through the manage.py file.

```bash
cd GymBuddyServer/
python3 manage.py runserver 0.0.0.0:8000
```

the server will be running on your local server and should allow all devices on your wifi to connect to it.

## admin

To enable administrative features on the server, you need to create a superuser. To do this, you can use the manage.py file.

```bash
python3 manage.py createsuperuser
```

with this you can go into your browser and access the server at "http://{your_ip_address}:8000/admin/"
Type in your superuser details and you can view all objects stored in the server and on the database
