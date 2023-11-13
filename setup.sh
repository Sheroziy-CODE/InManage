#!/bin/bash

# Exit script if any command fails
set -e

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python3 manage.py migrate

# Collect static files
python3 manage.py collectstatic --noinput

# Load initial data
python3 manage.py loaddata initial_data.json

# Update passwords
python3 update_passwords.py
