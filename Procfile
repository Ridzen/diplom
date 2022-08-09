worker: sh -c 'export $(cat .env | xargs)'
web: gunicorn mlbb.wsgi --log-file -
