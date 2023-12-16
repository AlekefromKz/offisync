FROM python:3.10-slim
ENV PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get install -y build-essential libpq-dev \
    && apt-get clean

# Upgrade pip
RUN pip install --upgrade pip

WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY offisync/* /app
