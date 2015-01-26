# celery-flower-docker
Docker container for monitoring celery

## Running with docker

In order to run flower using  docker , run
command: 

```
sudo docker run -it --rm --name cluster-deployer -p 5555:5555 totem/celery-flower-docker
```

## Access Flower

To access flower go to url:  
[http://172.17.42.1:5555](http://172.17.42.1:5555)

If your are using dynamic port mapping using (-P), inspect the container to determine the mapped
port for 5555.

## Run Configuration (Environment Variables)  
| Env Variable | Description | Default Value (Docker)|
| ------------ | ----------- |--------------------- |
| FLOWER_PORT | Port to be used by flower | 5555 |
| FLOWER_BROKER_API | API for broker. | http://guest:guest@172.17.42.1:15672/api/ |
| BROKER_URL | URL for the broker | amqp://guest:guest@172.17.42.1:5672 |
| FLOWER_MAX_TASKS | Max tasks to be stored in memory. | 3600 |
| FLOWER_BASIC_AUTH | Authentication for flower (username:passowrd) | root:changeit |
