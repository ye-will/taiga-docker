#!/bin/bash

chown -R taiga /taiga

echo "Waiting for Postgresql to be available..."
while ! nc -z ${DB_HOST} ${DB_PORT}; do
  sleep 1
done

su taiga << EOF
python manage.py migrate --noinput
python manage.py loaddata initial_user
python manage.py loaddata initial_project_templates
python manage.py compilemessages
python manage.py collectstatic --noinput

gunicorn -w 3 -t 60 --pythonpath=. -b 0.0.0.0:8000 taiga.wsgi
EOF
