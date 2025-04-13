FROM python:3.11-slim

WORKDIR /app
COPY . .

ENV PYTHONPATH=/app

CMD ["python3", "app/test_allocation.py"]


# Added Kubernetes support
