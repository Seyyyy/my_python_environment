FROM python:3.8.2-slim

RUN mkdir /app

WORKDIR /app

RUN pip install numpy opencv-python

# install native opencv
RUN apt-get -y update
RUN apt-get -y install build-essential
RUN apt-get -y install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev