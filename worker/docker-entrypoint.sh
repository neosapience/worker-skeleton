#!/bin/sh
set -e

if [ "$1" = 'celery' ]; then
    shift
    exec celery worker -A=task_custom \
        --loglevel=info \
        --pool=gevent \
        --concurrency=100 \
        -Q=task_custom_queue "$@"
fi

exec "$@"
