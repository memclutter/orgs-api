FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /usr/src/orgs/
WORKDIR /usr/src/orgs/

ADD requirements.txt /usr/src/orgs/
RUN apk update \
 && apk add --virtual build-deps gcc python-dev musl-dev linux-headers \
 && apk add postgresql-dev
RUN pip install --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

ADD . /usr/src/orgs
ADD ./deploy/django/uwsgi.ini /usr/src/orgs
ADD ./deploy/django/run.sh /usr/src/orgs
RUN mkdir -p /usr/src/public \
 && mkdir -p /usr/src/run
VOLUME /usr/src/public
VOLUME /usr/src/run
