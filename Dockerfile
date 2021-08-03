FROM python:3.6-slim-buster
WORKDIR /my_directory
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
WORKDIR /my_directory/
CMD gunicorn -b 0.0.0.0:8000 --access-logfile - "wsgi:app"