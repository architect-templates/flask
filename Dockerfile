FROM python:3.9.12

WORKDIR /app

# Install dependencies
COPY requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

# Copy project
COPY . /app

# Instantiate database
RUN flask init-db
