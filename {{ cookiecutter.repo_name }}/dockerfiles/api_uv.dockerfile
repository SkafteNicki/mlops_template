FROM ghcr.io/astral-sh/uv:python{{ cookiecutter.python_version }}-alpine AS base

RUN apt update && \
    apt install --no-install-recommends -y build-essential gcc && \
    apt clean && rm -rf /var/lib/apt/lists/*

COPY src src/
COPY uv.lock uv.lock
COPY README.md README.md
COPY pyproject.toml pyproject.toml

RUN uv sync --frozen

ENTRYPOINT ["uv", "run", "uvicorn", "src.{{cookiecutter.project_name}}.api:app", "--host", "0.0.0.0", "--port", "8000"]
