FROM python:3.11.6

RUN mkdir /home/bot

WORKDIR /home/bot

COPY requirements.txt .

RUN pip install -U pip setuptools

RUN pip install -r requirements.txt