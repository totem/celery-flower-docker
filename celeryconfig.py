import os
AMPQ_USERNAME = os.getenv('AMQP_USERNAME', 'guest')
AMPQ_PASSWORD = os.getenv('AMQP_PASSWORD', 'guest')
AMQP_HOST = os.getenv('AMQP_HOST', '172.17.42.1')
AMQP_PORT = int(os.getenv('AMQP_PORT', '5672'))

DEFAULT_BROKER_URL = 'amqp://%s:%s@%s:%d'\
                     % (AMPQ_USERNAME, AMPQ_PASSWORD, AMQP_HOST, AMQP_PORT)

BROKER_URL = os.getenv('BROKER_URL', DEFAULT_BROKER_URL)
