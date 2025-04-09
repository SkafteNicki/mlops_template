#! /usr/bin/env bash

# Install dependencies from requirements.txt
pip install -r requirements.txt

# Install development dependencies from requirements_dev.txt
pip install -r requirements_dev.txt

# Install pre-commit hooks
pre-commit install --install-hooks
