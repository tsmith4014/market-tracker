FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates curl gnupg \
 && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir awscli==1.34.14

WORKDIR /app
COPY app/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY app/market_tracker.py /app/market_tracker.py
COPY app/backtest.py /app/backtest.py
COPY app/report.py /app/report.py
COPY app/config.json /app/config.json
COPY app/symbols.json /app/symbols.json
COPY app/symbol_manager.py /app/symbol_manager.py
COPY app/symbol_search.py /app/symbol_search.py

VOLUME ["/data"]

CMD ["python", "/app/market_tracker.py"]
