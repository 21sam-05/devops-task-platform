FROM python:3.12-slim

LABEL org.opencontainers.image.source="https://github.com/21sam-05/devops-task-platform"

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app

EXPOSE 8000

CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]