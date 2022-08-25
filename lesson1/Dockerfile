FROM harbor.mobagel.com/core-tech-ci/python:3.8-slim as base

RUN apt-get update && pip3 install --upgrade pip

FROM base as builder

RUN mkdir /install

WORKDIR /install

COPY ./src/requirements.txt /requirements/requirements.txt

RUN pip install --prefix=/install -r /requirements/requirements.txt

FROM base

COPY --from=builder /install /usr/local

WORKDIR /app
COPY ./src /app
