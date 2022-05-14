FROM python:3.8
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
COPY wait-for /app/wait-for
RUN chmod +x ./wait-for
RUN pip install -r requirements.txt
RUN apt-get -q update && apt-get -qy install netcat
COPY . /app
