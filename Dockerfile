FROM python:3.10.8-slim


RUN apt-get update
WORKDIR /usr/src/app

COPY ./requirements.txt /usr/src/app

RUN pip install -r requirements.txt

COPY . /usr/src/app

CMD ./run.sh
