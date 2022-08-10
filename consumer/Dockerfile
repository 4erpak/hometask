FROM python:3-slim-buster

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY consumer.py .

CMD ["python", "./consumer.py"]
