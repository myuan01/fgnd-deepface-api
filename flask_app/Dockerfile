FROM python:3.6.12

WORKDIR usr/src/flask_app
COPY requirements.txt .
RUN apt-get update
RUN apt-get install 'ffmpeg'\
    'libsm6'\
    'libxrender-dev'\
    'libxext6'  -y
RUN pip install --no-cache-dir -r requirements.txt
COPY . .