# django_celery

A sample celery django app, that take input and return it back. 

Make sure reddis is installed. 

## Install packages
`pip install -r requirements.txt`

## Run django 
`python manage.py runserver`

## Run celery
`python -m celery -A project_celery worker`