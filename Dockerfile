from python:3.9-alpine

WORKDIR /code/

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

