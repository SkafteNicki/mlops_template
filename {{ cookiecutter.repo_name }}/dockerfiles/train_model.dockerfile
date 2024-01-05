# Base image
FROM python:{{ cookiecutter.python_version }}-slim

RUN apt update && \
    apt install --no-install-recommends -y build-essential gcc && \
    apt clean && rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt
COPY pyproject.toml pyproject.toml
COPY {{cookiecutter.project_name}}/ {{cookiecutter.project_name}}/
COPY data/ data/

WORKDIR /
RUN pip install -r requirements.txt --no-cache-dir
RUN pip install . --no-deps --no-cache-dir

ENTRYPOINT ["python", "-u", "{{ cookiecutter.project_name }}/train_model.py"]