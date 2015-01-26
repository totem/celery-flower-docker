import os
BROKER_URL = os.getenv('BROKER_URL',
                       'amqp://guest:guest@172.17.42.1:5672')
