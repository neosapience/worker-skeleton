from . import celery_app
from .setup import logger


@celery_app.task
def my_task(param1):
    return param1
