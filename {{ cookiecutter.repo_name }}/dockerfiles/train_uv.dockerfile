FROM ghcr.io/astral-sh/uv:python{{ cookiecutter.python_version }}-alpine AS base

COPY src src/
COPY uv.lock uv.lock
COPY README.md README.md
COPY pyproject.toml pyproject.toml

RUN uv sync --frozen

ENTRYPOINT ["uv", "run", "src/{{ cookiecutter.project_name }}/train.py"]
