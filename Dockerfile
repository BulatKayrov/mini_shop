FROM python:3.10

WORKDIR app

COPY req.txt .

RUN pip install -r req.txt

COPY . .

RUN chmod a+x /app/docker/*.sh

# Определяем команду, чтобы начать приложение
#CMD gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000