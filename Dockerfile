FROM python:3.7

COPY ["requeriments.txt" ,  "/app/"]

WORKDIR /app

RUN pip install -r requeriments.txt

COPY ["." ,  "/app/"]

EXPOSE 8000