#!/bin/bash

rm celery*.pid celery*.log
celery multi start 4 -A scanner.jobs --pool=eventlet --concurrency=1000

rm celerybeat.pid
celery beat -A scanner.jobs -s /tmp/celerybeat
