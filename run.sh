#!/bin/bash

export DB_DIR='$HOME/Projects/databases'
# export DATABASE_URL = # to be defined later

export FLASK_APP=backend/backend.py
flask run