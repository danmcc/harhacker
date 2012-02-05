import os

BROKER_HOST = os.environ.get('BROKER_HOST', 'localhost')
BROKER_PORT = int(os.environ.get('BROKER_PORT', 5672))
BROKER_USER = os.environ.get('BROKER_USER', 'guest')
BROKER_PASSWORD = os.environ.get('BROKER_PASSWORD', 'guest')
BROKER_VHOST = os.environ.get('BROKER_VHOST', '/')

CELERY_RESULT_BACKEND = 'amqp'
