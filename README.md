# celery-flower-docker
Docker container for monitoring celery

## Running with docker

In order to run flower using  docker , run
command: 

```
sudo docker run -it --rm --name cluster-deployer -p 5555:5555 totem/celery-flower-docker
```

## Access Flower

To access flower go to url:  [http://172.17.42.1:5555](http://172.17.42.1:5555).  
The default credentials for the flower instance is username:root  password:changeit. 
(It is highly recommended to change the default credentials. See run configuration.)

If your are using dynamic port mapping using (-P), inspect the container to determine the mapped
port for 5555.

## Run Configuration (Environment Variables)  
| Env Variable | Description | Default Value (Docker)|
| ------------ | ----------- |--------------------- |
| FLOWER_PORT | Port to be used by flower | 5555 |
| AMQP_USERNAME | Rabbitmq broker username | guest |
| AMQP_PASSWORD | Rabbitmq broker password | guest |
| AMQP_HOST | Rabbitmq host | 172.17.42.1 |
| AMQP_PORT | Rabbitmq port | 5672 |
| AMQP_ADMIN_USERNAME | Rabbitmq admin username | guest |
| AMQP_ADMIN_PASSWORD | Rabbitmq admin password | guest |
| AMQP_ADMIN_HOST | Rabbitmq admin host | 172.17.42.1 |
| AMQP_ADMIN_PORT | Rabbitmq admin port | 15672 |
| FLOWER_MAX_TASKS | Max tasks to be stored in memory. | 3600 |
| FLOWER_BASIC_AUTH | Authentication for flower (username:passowrd) | root:changeit |
