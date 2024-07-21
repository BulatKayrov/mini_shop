from celery import Celery

from config import settings

app = Celery(
    main='celery',
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL,
    include=['tasks.task']
)
