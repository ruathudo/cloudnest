FROM python:3
MAINTAINER Quan Duong <quan.duong.vn@gmail.com>

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY boot.sh ./
COPY . ./
ENTRYPOINT ["./boot.sh"]
