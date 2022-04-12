FROM python:3.9.12

WORKDIR /app

# Install dependencies
COPY requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

# Copy project
COPY . /app

# Set environment variables
ENV FLASK_APP=flaskr
ENV FLASK_ENV=development
ENV FLASK_HOST=0.0.0.0
ENV FLASK_PORT=5000

# Instantiate database
RUN flask init-db
