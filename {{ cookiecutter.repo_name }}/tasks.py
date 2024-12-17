import os
from invoke import task

WINDOWS = os.name == "nt"
PROJECT_NAME = "{{ cookiecutter.repo_name }}"
PYTHON_VERSION = "{{ cookiecutter.python_version }}"

# Setup commands
@task
def create_enviroment(ctx):
    ctx.run(
        f"conda create --name {PROJECT_NAME} python={PYTHON_VERSION} pip --no-default-packages --yes",
        echo=True,
        pty=not WINDOWS,
    )

@task
def requirements(ctx):
    ctx.run("pip install -U pip setuptools wheel", echo=True, pty=not WINDOWS)
    ctx.run("pip install -r requirements.txt", echo=True, pty=not WINDOWS)
    ctx.run("pip install -e .", echo=True, pty=not WINDOWS)


@task(requirements)
def dev_requirements(ctx):
    ctx.run("pip install -e .[\"dev\"]", echo=True, pty=not WINDOWS)


@task
def clean(ctx):
    ctx.run("find . -type f -name \"*.py[co]\" -delete", echo=True, pty=not WINDOWS)
    ctx.run("find . -type d -name \"__pycache__\" -delete")

# Project commands
@task
def preprocess_data(ctx):
    ctx.run(f"python src/{PROJECT_NAME}/data.py data/raw data/processed", echo=True, pty=not WINDOWS)

@task
def train(ctx):
    ctx.run(f"python src/{PROJECT_NAME}/train.py", echo=True, pty=not WINDOWS)

@task
def test(ctx):
    ctx.run("coverage run -m pytest tests/", echo=True, pty=not WINDOWS)
    ctx.run("coverage report -m", echo=True, pty=not WINDOWS)

@task
def docker_build(ctx):
    ctx.run("docker build -t train:latest dockerfiles/ -f dockerfiles/train.Dockerfile", echo=True, pty=not WINDOWS)
    ctx.run("docker build -t api:latest dockerfiles/ -f dockerfiles/api.Dockerfile", echo=True, pty=not WINDOWS)

# Documentation commands
@task(dev_requirements)
def build_docs(ctx):
    ctx.run("mkdocs build --config-file docs/mkdocs.yaml --site-dir build", echo=True, pty=not WINDOWS)


@task(dev_requirements)
def serve_docs(ctx):
    ctx.run("mkdocs serve --config-file docs/mkdocs.yaml", echo=True, pty=not WINDOWS)
