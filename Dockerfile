FROM python:3.8
ENV PYTHONUNBUFFERED 1

#Dir for app
WORKDIR /app

#script for order to startup
COPY wait-for /app/wait-for
RUN chmod +x ./wait-for

#librery to wait for
RUN apt-get -q update && apt-get -qy install netcat

#Install requirements
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . /app
