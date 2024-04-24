FROM python:3.8-slim-bullseye
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends 
RUN apt-get update && apt-get install -y libgomp1

WORKDIR /app

COPY ./server/ /app/

EXPOSE 8080
EXPOSE 8081

WORKDIR /app

RUN pip3 install -r requirements.txt
CMD while true; do python3 main.py; done
