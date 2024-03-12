set PGPASSWORD=admin
pg_dump -h "localhost" -U "postgres" -f "F:\GitHub\study-django\web-django-practice-4\backup\backup2.dump" "django_db"