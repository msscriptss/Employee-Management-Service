# syntax==docker/dockerfile:1

FROM python:3.8-slim-buster

RUN mkdir /app
WORKDIR /app

ENV FLASK_APP run.py

RUN apt-get update && apt-get install -y sqlite3 libsqlite3-dev
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Copy project directory in workdir (/app)
COPY . .

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]