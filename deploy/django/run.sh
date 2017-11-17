#!/usr/bin/env sh

# wait for postgresql up and running
sleep 6

python manage.py migrate --no-input
python manage.py loaddata api/v1/fixtures/articles.json
python manage.py loaddata api/v1/fixtures/categories.json
python manage.py loaddata api/v1/fixtures/districts.json
python manage.py loaddata api/v1/fixtures/networks.json
python manage.py loaddata api/v1/fixtures/organizations.json
python manage.py loaddata api/v1/fixtures/productions.json
python manage.py loaddata api/v1/fixtures/users.json
python manage.py collectstatic --no-input

uwsgi --ini uwsgi.ini
