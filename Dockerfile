FROM python:3.5.0

RUN pip install flower==0.8.3

ADD celeryconfig.py /opt/celery-flower/
ADD flowerconfig.py /opt/celery-flower/
WORKDIR /opt/celery-flower

EXPOSE 5555

ENTRYPOINT ["/usr/local/bin/celery"]

CMD ["--loglevel=info", "flower"]
