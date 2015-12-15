from    __future__              import absolute_import



# This will make sure the app is always imported when
from    .celery                 import app as celery_app

__all__ = ['celery_app']
