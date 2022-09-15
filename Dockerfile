FROM alpine:edge

MAINTAINER <support@collectiveacuity.com>

# Update Alpine environment
RUN echo '@edge http://nl.alpinelinux.org/alpine/edge/main' >> /etc/apk/repositories
RUN echo '@community http://nl.alpinelinux.org/alpine/edge/community' >> /etc/apk/repositories
RUN echo '@testing http://nl.alpinelinux.org/alpine/edge/testing' >> /etc/apk/repositories
RUN apk update
RUN apk upgrade
RUN apk add ca-certificates

# Install Python & Pip
RUN apk add curl
RUN apk add python3
RUN curl -sS https://bootstrap.pypa.io/get-pip.py | python3

# Install C Compiler Dependencies
RUN apk add gcc
RUN apk add g++
RUN apk add python3-dev
RUN apk add postgresql-dev
RUN apk add libffi-dev

# Install Python Modules
RUN pip3 install flask
RUN pip3 install cffi
RUN pip3 install gunicorn
RUN pip3 install gevent
RUN pip3 install requests

# Clean APK cache
RUN rm -rf /var/cache/apk/*

ENV SYSTEM_ENVIRONMENT=prod
ENV SYSTEM_PLATFORM=heroku
ADD ./cred /opt/cred
ADD ./data /opt/data
ADD ./server /opt/server
CMD gunicorn -k gevent -w 1 --chdir /opt/server launch:app -b 0.0.0.0:$PORT