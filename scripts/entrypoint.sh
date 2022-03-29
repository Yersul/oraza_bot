python manage.py makemigrations
python manage.py migrate

python manage.py collectstatic --no-input
# python manage.py runserver 0.0.0.0:8000
gunicorn oraza_bot.wsgi:application --bind 0.0.0.0:8000