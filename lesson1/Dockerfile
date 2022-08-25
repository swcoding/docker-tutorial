FROM harbor.mobagel.com/core-tech-ci/python:3.8-slim as base

RUN apt-get update && pip3 install --upgrade pip && pip install poetry

WORKDIR /app
COPY pyproject.toml poetry.lock .

RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi --no-dev

COPY ./backend /app

# RUN pip install --prefix=/install -r /requirements/requirements.txt

# FROM base

# COPY --from=builder /install /usr/local

# WORKDIR /app
# COPY ./src /app
