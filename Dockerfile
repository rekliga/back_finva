FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install poetry && poetry install
RUN poetry install --no-root --no-interaction --no-ansi
CMD ["poetry", "run", "uvicorn", "app.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
