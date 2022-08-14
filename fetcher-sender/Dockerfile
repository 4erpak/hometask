FROM python:3-slim-buster

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY twitter_fetcher.py .

CMD ["python", "./twitter_fetcher.py"]
