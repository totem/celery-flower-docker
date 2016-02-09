import os

AMPQ_ADMIN_USERNAME = os.getenv('AMQP_ADMIN_USERNAME', 'guest')
AMPQ_ADMIN_PASSWORD = os.getenv('AMQP_ADMIN_PASSWORD', 'guest')
AMQP_ADMIN_HOST = os.getenv('AMQP_ADMIN_HOST', '172.17.42.1')
AMQP_ADMIN_PORT = int(os.getenv('AMQP_ADMIN_PORT', '15672'))

DEFAULT_BROKER_API = 'http://%s:%s@%s:%d/api/' \
                     % (AMPQ_ADMIN_USERNAME, AMPQ_ADMIN_PASSWORD,
                        AMQP_ADMIN_HOST, AMQP_ADMIN_PORT)
USERNAME = os.getenv('USERNAME', 'root')
PASSWORD = os.getenv('PASSWORD', 'changeit')

port = int(os.getenv('FLOWER_PORT', '5555'))
broker_api = os.getenv('FLOWER_BROKER_API', DEFAULT_BROKER_API)
max_tasks = int(os.getenv('FLOWER_MAX_TASKS', '3600'))
basic_auth = [os.getenv('FLOWER_BASIC_AUTH', '%s:%s'
                        % (USERNAME, PASSWORD))]
