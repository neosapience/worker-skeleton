from celery import Celery
from celery.signals import after_setup_logger
import logging

celery_app = Celery(__name__)
celery_app.config_from_object('app_settings.Config')
logger = logging.getLogger(__name__)

celery_app.conf.task_routes = {
    'task_custom.*': {'queue': 'task_custom_queue'},
}


@after_setup_logger.connect
def setup_loggers(logger, *args, **kwargs):
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # SysLogHandler
    slh = logging.handlers.SysLogHandler(address=('localhost', 514))
    slh.setFormatter(formatter)
    logger.addHandler(slh)
