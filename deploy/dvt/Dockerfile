FROM python:3.8

RUN apt-get update && apt-get upgrade -y && apt-get install -y
RUN apt-get install -y apt-utils
RUN apt-get install -y build-essential mediainfo ffmpeg

WORKDIR /app/src/
ADD ./requires.txt /app/
RUN cd /app/ && pip install --no-cache-dir -r requires.txt

ADD ./deploy/dvt/start-django-dev.sh /app/
ADD ./deploy/dvt/start-celery-worker.sh /app/
RUN chmod +x /app/*.sh
EXPOSE 8000
ADD ./src/ /app/src/
