FROM python:3.9-buster

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8081

ENTRYPOINT [ "python", "-m", "flaskr.app" ]
