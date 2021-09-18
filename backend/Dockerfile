FROM python:3.9-buster

WORKDIR /app

COPY app.py .
COPY requirements.txt .
COPY data/ .

RUN pip install -r -requirements.txt

EXPOSE 8081

ENTRYPOINT [ "python", "app.py" ]