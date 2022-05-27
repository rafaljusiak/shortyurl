# Pull base image
FROM python:3.10-slim

RUN pip install --upgrade pip

COPY ./requirements/requirements.txt .
COPY ./requirements/requirements-dev.txt .
RUN pip3 install -r requirements-dev.txt

COPY ./docker/django/wait-for-postgres.py /wait-for-postgres.py
RUN chmod +x /wait-for-postgres.py

COPY ./docker/django/run.sh /run.sh
RUN chmod +x /run.sh

WORKDIR /app

ENTRYPOINT ["bash", "/run.sh"]
