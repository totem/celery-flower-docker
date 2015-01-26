FROM totem/python-base:2.7-trusty

ADD requirements.txt /opt/celery-flower/
RUN pip install -r /opt/celery-flower/requirements.txt

ADD celeryconfig.py /opt/celery-flower/
ADD flowerconfig.py /opt/celery-flower/
WORKDIR /opt/celery-flower

EXPOSE 5555

ENTRYPOINT ["/usr/local/bin/celery"]
CMD ["--loglevel=info","-P", "gevent", "flower"]
