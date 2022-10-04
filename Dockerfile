FROM python:3.9.12

ENV FLASK_APP src

WORKDIR /api

# Install dependencies
COPY requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

# Copy project
COPY . /api
