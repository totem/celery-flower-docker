import os
port = int(os.getenv('port', '5555'))
broker_api = os.getenv('FLOWER_BROKER_API',
                       'http://guest:guest@172.17.42.1:15672/api/')
max_tasks = int(os.getenv('FLOWER_MAX_TASKS', '3600'))
basic_auth = [os.getenv('FLOWER_BASIC_AUTH', 'root:changeit')]
