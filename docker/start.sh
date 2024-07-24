#!/bin/bash

sleep 5
alembic revision --autogenerate -m "created all tables"
alembic upgrade head

uvicorn main:app --host 0.0.0.0 --port 8000
#gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000