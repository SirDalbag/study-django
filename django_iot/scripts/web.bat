call venv.bat

cd web

python manage.py migrate

python manage.py runserver