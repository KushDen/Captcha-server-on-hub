FROM python:3.7.3
MAINTAINER Denis Kushchuk 'dkuschuk@ispras.ru'
RUN apt-get update -y
RUN apt-get install -y python3-pip 
RUN pip3 install -U pip
WORKDIR /app
COPY requirements.txt /app
RUN pip3 install -r requirements.txt
COPY . /app
CMD ["python3", "-u", "app.py"]

