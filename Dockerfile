FROM python:3.8.1

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /usr/src/app
WORKDIR /usr/src/app

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
COPY src/requirements.txt /usr/src/app/
RUN pip install -r requirements.txt

COPY src/. /usr/src/app/
