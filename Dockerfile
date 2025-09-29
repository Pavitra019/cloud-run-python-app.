Use the official lightweight Python image.
https://hub.docker.com/_/python
FROM python:3.11-slim

Set the working directory inside the container
WORKDIR /app

Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

Copy the rest of the application code
COPY . .

Set the environment variable for the port
ENV PORT 8080

Run the web service using Gunicorn
CMD exec gunicorn --workers=1 --threads=8 --bind 0.0.0.0:8080 app:app