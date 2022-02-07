# Veterinary Application using Django

## Setup

-The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/BeyzaaKoroglu/Veterinary-Application.git
$ cd sample-django-app
```

-Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv --python=3.8 .venv
$ source .venv/bin/activate
```

-Then install the dependencies:

```sh
$ cd vetApp
$ pip install -r requirements.txt
```

-Create server, database and superuser with the Postgresql.

-Execute the migrate process:

```sh
$ python manage.py migrate
```

-Copy .env.dist file as .env and fill in the contents of .env


### Inside of the ".env" File
- Generate SECRET_KEY in the .env file:

```sh
$ python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

- DEBUG variable should be True only during project development. 

- The parameters in the DATABASE_URL variable in the .env file are the superuser username and password, the IP and port specified for the server, and the database name, respectively.

## Run

```sh
$ python manage.py runserver
```