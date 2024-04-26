FROM python:{{ cookiecutter.python_version }}-slim-buster

RUN apt update && \
    apt install --no-install-recommends -y build-essential gcc && \
    apt clean && rm -rf /var/lib/apt/lists/*
