FROM ghcr.io/astral-sh/uv:python{{ cookiecutter.python_version }}-alpine AS base

COPY src src/
COPY uv.lock uv.lock
COPY README.md README.md
COPY pyproject.toml pyproject.toml

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --compile-bytecode

ENTRYPOINT ["uv", "run", "uvicorn", "src.{{cookiecutter.project_name}}.api:app", "--host", "0.0.0.0", "--port", "8000"]
