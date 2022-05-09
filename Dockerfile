FROM python:3.9.12-slim

RUN apt-get update && \
    apt-get install -y libpq-dev gcc

RUN mkdir -p UrlShortner-api

WORKDIR UrlShortner-api


ADD requirements.txt .
RUN pip install -r requirements.txt

ADD core core
ADD api api

CMD ["/bin/bash"]
