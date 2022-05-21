FROM python:3.10-buster


RUN mkdir /model
WORKDIR /model
Add https://alphacephei.com/vosk/models/vosk-model-small-ja-0.22.zip /model/vosk-model-small-ja-0.22.zip
RUN unzip /model/vosk-model-small-ja-0.22.zip

COPY src /src
WORKDIR /src

RUN apt-get update && \
    apt-get install -y libsndfile1 && \
    apt-get -y clean && \
    rm -rf /var/lib/apt/lists/*
RUN pip install -r requirements.txt