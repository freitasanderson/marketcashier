#!/bin/sh

# O shell irá encerrar a execução do script quando um comando falhar
set -e

git pull origin main --force

python manage.py collectstatic --noinput
python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py shell -c "from django.contrib.auth.models import User; \
                           User.objects.filter(username='meire').exists() or \
                           User.objects.create_superuser('meire',
                           'meire@example.com', 'mercadosena')"
python manage.py runserver 0.0.0.0:1404
