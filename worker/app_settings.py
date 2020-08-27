import os
import logging
from distutils.util import strtobool
from kombu.utils.url import safequote


class Config(object):
    MONGO_HOST = os.environ.get('MONGO_HOST', 'mongo')
    MONGO_DBNAME = os.environ.get('MONGO_DBNAME', 'light')
    MONGO_USER = os.environ.get('MONGO_USERNAME', '')
    MONGO_PASS = os.environ.get('MONGO_PASSWORD', '')
    MONGO_RSNAME = os.environ.get('MONGO_RSNAME', '')

    mongo_uri_params = []
    if not MONGO_USER:
        MONGO_URI = f'mongodb://{MONGO_HOST}/{MONGO_DBNAME}'
    else:
        mongo_uri_params.append('authSource=admin')
        MONGO_URI = f'mongodb://{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}/{MONGO_DBNAME}'

    if MONGO_RSNAME:
        mongo_uri_params.append(f'replicaSet={MONGO_RSNAME}')

    MONGO_URI += '?' + '&'.join(mongo_uri_params)

    REDIS_URL = 'redis://:{}@{}:6379/0'.format(
        os.environ.get('REDIS_PASSWORD', ''),
        os.environ.get('REDIS_HOST', 'redis'))

    _redis_url = 'redis://:{}@{}:6379/0'.format(
        os.environ.get('REDIS_PASSWORD', ''),
        os.environ.get('REDIS_HOST', 'redis'))

    if 'sqs' == os.environ.get('WORKER_QUEUE_BROKER'):
        sqs_aws_access_key = safequote(os.environ['SQS_ACCESS_KEY'])
        sqs_aws_secret_key = safequote(os.environ['SQS_SECRET_KEY'])
        BROKER_TRANSPORT_OPTIONS = {
            'queue_name_prefix': os.environ['WORKER_QUEUE_PREFIX']
        }
        BROKER_URL = f'sqs://{sqs_aws_access_key}:{sqs_aws_secret_key}@'
    else:
        BROKER_URL = _redis_url

    CELERY_RESULT_BACKEND = _redis_url
    CELERY_TIMEZONE = 'Asia/Seoul'
    CELERY_ALWAYS_EAGER = strtobool(os.environ.get('CELERY_ALWAYS_EAGER', 'false'))
    CELERY_ENABLE_UTC = False
