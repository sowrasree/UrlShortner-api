FROM python:3.9.12-slim

RUN apt-get update && \
    apt-get install -y libpq-dev gcc

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.9.0/wait /wait
RUN chmod +x /wait

RUN mkdir -p UrlShortner-api

WORKDIR UrlShortner-api


ADD requirements.txt .
RUN pip install -r requirements.txt

ADD gunicorn_config.py gunicorn_config.py
ADD run.sh run.sh
ADD core core

CMD ["/bin/bash"]
