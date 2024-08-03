#!/usr/bin/env python
import sys
from pathlib import Path, PurePath


def create_project_directory(project_name):
    project_path = Path(project_name)
    structure = [
        ".gitignore",
        "README.md",
        "pyproject.toml",
        "poetry.lock",
        PurePath("src").joinpath(project_name, "__init__.py"),
        PurePath("src").joinpath(project_name, "module1.py"),
        PurePath("src").joinpath(project_name, "module2.py"),
        PurePath("src").joinpath(project_name, "cli.py"),
        PurePath("src").joinpath(project_name, "services", "service1.py"),
        PurePath("src").joinpath(project_name, "utils.py"),
        PurePath("src").joinpath(project_name, "config", "settings.py"),
        PurePath("src").joinpath(project_name, "business_logic", "__init__.py"),
        PurePath("src").joinpath(project_name, "business_logic", "logic1.py"),
        PurePath("tests").joinpath("__init__.py"),
        PurePath("tests").joinpath("test_module1.py"),
        PurePath("tests").joinpath("test_module2.py"),
        PurePath("tests").joinpath("test_cli.py"),
        "Dockerfile",
        PurePath(".github").joinpath("workflows", "ci.yml"),
        ".coveragerc",
        "run_tests.sh",
    ]

    for file_path in structure:
        full_path = project_path / file_path
        full_path.parent.mkdir(parents=True, exist_ok=True)
        if not full_path.exists():
            full_path.touch()

    with open(project_path / "README.md", "w", encoding="utf-8") as f:
        f.write(
            "# "
            + project_name.capitalize()
            + "\n\nA short description of your project.\n"
        )

    with open(project_path / ".gitignore", "w", encoding="utf-8") as f:
        f.write("*.pyc\n__pycache__/\n.env\n")

    with open(project_path / "pyproject.toml", "w", encoding="utf-8") as f:
        f.write(
            f"""[tool.poetry]
name = "{project_name}"
version = "0.1.0"
description = "A short description of your project"
authors = ["Your Name <you@example.com>"]

[tool.poetry.dependencies]
python = "^3.12"
requests = "^2.25.1"

[tool.poetry.dev-dependencies]
pytest = "^6.2.4"
coverage = "^5.5"
flake8 = "^3.9.2"
black = "^21.7b0"

[tool.coverage.run]
branch = true
source = ["src"]

[tool.coverage.report]
show_missing = true

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"

[tool.poetry.scripts]
your-cli = "{project_name}.cli:main"

[tool.black]
line-length = 79
target-version = ['py312']

[tool.flake8]
max-line-length = 79
"""
        )

    with open(project_path / ".coveragerc", "w", encoding="utf-8") as f:
        f.write(
            """[run]
source = .
parallel = true
"""
        )

    with open(project_path / "Dockerfile", "w", encoding="utf-8") as f:
        f.write(
            f"""FROM python:3.12-alpine

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN pip install poetry && poetry install --no-dev

COPY src/ .

CMD ["poetry", "run", "python", "src/{project_name}/main.py"]
"""
        )

    with open(
        project_path / PurePath(".github").joinpath("workflows", "ci.yml"),
        "w",
        encoding="utf-8",
    ) as f:
        f.write(
            """name: CI

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - uses: actions/setup-python@v2
      with:
        python-version: '3.12'
    - name: Install dependencies
      run: |
        pip install poetry
        poetry install
    - name: Run tests and coverage
      run: ./run_tests.sh
    - name: Upload coverage report
      uses: actions/upload-artifact@v2
      with:
        name: coverage-report
        path: htmlcov/
"""
        )

    with open(project_path / "run_tests.sh", "w", encoding="utf-8") as f:
        f.write(
            """#!/bin/bash

# Run tests with coverage
poetry run coverage run --source=src -m pytest

# Run CLI tests
poetry run coverage run --source=src --append -m pytest tests/test_cli.py

# Combine coverage data
poetry run coverage combine

# Generate coverage report
poetry run coverage report
poetry run coverage html
"""
        )

    Path(project_path / "run_tests.sh").chmod(0o755)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        project_name = sys.argv[1]
    else:
        project_name = input("Enter the project name: ")
    create_project_directory(project_name)
    print(f"Project {project_name} structure created successfully.")
