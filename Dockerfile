FROM ubuntu:18.04
MAINTAINER Denis Kushchuk 'dkuschuk@ispras.ru'
RUN apt-get update -y
RUN apt-get install -y python3.8
RUN apt-get install -y python3-pip 
RUN apt-get install -y python3-dev build-essential
RUN pip3 install -U pip
WORKDIR /app
COPY requirements.txt /app
RUN pip3 install -r requirements.txt
COPY . /app
EXPOSE 5000
CMD ["python3", "-u", "app.py", "runserver", "0.0.0.0:5000"]

