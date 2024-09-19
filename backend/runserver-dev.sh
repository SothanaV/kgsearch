python manage.py migrate
python manage.py shell < script/createsupseruser.py
python manage.py shell < script/init-data.py
python manage.py runserver 0.0.0.0:8000