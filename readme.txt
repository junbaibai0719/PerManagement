python -m pip install mysqlclient
python manage.py startapp permanage
python manage.py inspectdb > permanage/models.py
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 127.0.0.1:8000