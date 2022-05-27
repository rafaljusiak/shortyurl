#!/usr/bin/env bash

python3 /wait-for-postgres.py
python3 manage.py runserver 0.0.0.0:8000
