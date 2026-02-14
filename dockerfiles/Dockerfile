FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
  gcc \
  libxml2-dev \
  libxslt1-dev \
  libffi-dev \
  build-essential \
  curl \
&& rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

COPY . . 

EXPOSE 4200

