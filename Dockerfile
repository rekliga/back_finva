FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y curl build-essential libpq-dev

COPY pyproject.toml poetry.lock* ./

RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="/root/.local/bin:${PATH}"

RUN poetry --version

RUN poetry config virtualenvs.create false

RUN poetry install --no-interaction --no-ansi

COPY . .

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "app.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
