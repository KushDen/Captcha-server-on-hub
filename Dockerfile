FROM ubuntu:18.04
MAINTAINER Denis Kushchuk 'dkuschuk@ispras.ru'
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY . /app
COPY modelForYandexCPU.h5 /app
EXPOSE 5000
CMD ["python3", "-u", "app.py", "runserver", "0.0.0.0:5000"]

