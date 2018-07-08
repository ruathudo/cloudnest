#!/bin/sh
flask db upgrade

if [ $FLASK_ENV = development ]
then
    exec python3 -m flask run --host 0.0.0.0 --port 5000
else
    exec gunicorn -w 1 -b 0.0.0.0:5000 run:app
fi