import os
AMPQ_USERNAME = os.getenv('AMPQ_USERNAME', 'guest')
AMPQ_PASSWORD = os.getenv('AMPQ_PASSWORD', 'guest')
AMQP_HOST = os.getenv('AMPQ_HOST', '172.17.42.1')
AMQP_PORT = int(os.getenv('AMPQ_PORT', '5672'))

DEFAULT_BROKER_URL = 'amqp://%s:%s@%s:%d'\
                     % (AMPQ_USERNAME, AMPQ_PASSWORD, AMQP_HOST, AMQP_PORT)

BROKER_URL = os.getenv('BROKER_URL', DEFAULT_BROKER_URL)
