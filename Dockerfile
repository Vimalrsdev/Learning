# Use official Python slim image

FROM python:3.11-slim

ENV PYTHONBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt 
COPY . .

EXPOSE 5000
ENV FLASK_APP=project.py
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]



