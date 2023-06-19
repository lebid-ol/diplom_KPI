release: python manage.py makemigrations && python manage.py migrate
web: gunicorn scraping_service.wsgi