# django-template
Django template

Starting commands for local dev

pipenv install

pipenv shell

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

## Starting commands for production

pip install -r requirements.txt

Make sure server ip is in allowed hosts in settings.py

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

nohup python manage.py runserver