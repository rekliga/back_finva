FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install poetry && poetry install

CMD ["poetry", "run", "uvicorn", "app.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
