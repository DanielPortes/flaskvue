#!/bin/sh

echo "Waiting for database..."
dockerize -wait tcp://db:5432

echo "Running database migrations..."
flask db upgrade

echo "Starting Flask application..."
python run.py --host='0.0.0.0'
