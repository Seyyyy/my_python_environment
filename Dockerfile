FROM python:3.8.2-slim

RUN mkdir /app

WORKDIR /app

RUN pip install numpy opencv-python

# install native opencv
RUN apt-get update
RUN apt-get install build-essential
RUN apt-get install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev