FROM python:3.10.8-slim


RUN apk update && \
    apk add --virtual build-deps gcc python-dev musl-dev && \
    apk add netcat-openbsd

WORKDIR /usr/src/app

COPY ./requirements.txt /usr/src/app

RUN pip install -r requirements.txt

COPY . /usr/src/app

CMD ./run.sh