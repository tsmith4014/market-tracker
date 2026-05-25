FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app

WORKDIR /app

COPY app/requirements.txt /app/requirements.txt
COPY app/requirements-dev.txt /app/requirements-dev.txt
RUN pip install --no-cache-dir -r /app/requirements.txt \
    && pip install --no-cache-dir -r /app/requirements-dev.txt

COPY app/ /app/

VOLUME ["/data"]

CMD ["python", "/app/market_tracker.py"]
