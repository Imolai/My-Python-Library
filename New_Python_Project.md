# New Python Project

Modern Python Project Structure in 2024. Creating a Python project in 2024 requires adhering to the
latest best practices to ensure maintainability, scalability, and ease of collaboration. This guide
will walk you through the recommended steps and structure for a modern Python project.

## Contents

- [New Python Project](#new-python-project)
  - [Contents](#contents)
  - [Project Structure](#project-structure)
  - [`.coveragerc` File Content](#coveragerc-file-content)
  - [Test and Coverage Script](#test-and-coverage-script)
  - [`pyproject.toml` File Content](#pyprojecttoml-file-content)
  - [Dockerfile](#dockerfile)
  - [CI/CD Configuration](#cicd-configuration)
  - [Summary](#summary)
  - [Further Readings](#further-readings)

## Project Structure

A well-organized project structure is crucial. Here’s a recommended layout:

```console
project_root/
├── .gitignore
├── README.md
├── pyproject.toml
├── poetry.lock
├── src/
│   └── your_package/
│       ├── __init__.py
│       ├── module1.py
│       ├── module2.py
│       ├── cli.py
│       ├── services/
│       │   └── service1.py
│       ├── utils.py
│       ├── config/
│       │   └── settings.py
│       └── business_logic/
│           ├── __init__.py
│           └── logic1.py
├── tests/
│   ├── __init__.py
│   ├── test_module1.py
│   ├── test_module2.py
│   └── test_cli.py
├── Dockerfile
├── .github/
│   └── workflows/
│       └── ci.yml
└── .coveragerc
```

## `.coveragerc` File Content

```ini
[run]
source = .
parallel = true
```

## Test and Coverage Script

Create a script named `run_tests.sh` for running tests and combining coverage reports:

```bash
#!/bin/bash

# Run tests with coverage
poetry run coverage run --source=src -m pytest

# Run CLI tests
poetry run coverage run --source=src --append -m pytest tests/test_cli.py

# Combine coverage data
poetry run coverage combine

# Generate coverage report
poetry run coverage report
poetry run coverage html
```

Make sure to give execute permission to the script:

```bash
chmod +x run_tests.sh
```

## `pyproject.toml` File Content

Here’s a good starting content for the `pyproject.toml`:

```toml
[tool.poetry]
name = "your_project"
version = "0.1.0"
description = "A short description of your project"
authors = ["Your Name <you@example.com>"]

[tool.poetry.dependencies]
python = "^3.12"
# Add your dependencies here
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
your-cli = "your_package.cli:main"

[tool.black]
line-length = 79
target-version = ['py312']

[tool.flake8]
max-line-length = 79
```

## Dockerfile

```Dockerfile
FROM python:3.12-alpine

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN pip install poetry && poetry install --no-dev

COPY src/ .

CMD ["poetry", "run", "python", "src/your_package/main.py"]
```

## CI/CD Configuration

Here's a simple CI configuration for GitHub Actions:

```yaml
# .github/workflows/ci.yml
name: CI

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
```

## Summary

This setup ensures that your Python project is modern, well-structured, and ready for development,
testing, containerization, and continuous integration/deployment using Python 3.12. By following
these practices, you can maintain a high-quality codebase that is easy to manage and collaborate on.

> Here in the directory you will find the [new_python_project.py](./new_python_project.py) script
> that will help you create these files for your new project.

Here is a consolidated list of commands to get your project up and running after the script
execution:

```bash
# Navigate to your new project directory
cd new-project

# Install Poetry if it is needed
pip install poetry

# Initialize and install dependencies with Poetry
poetry install

# Activate the virtual environment
poetry shell

# Run initial tests
./run_tests.sh

# Check code formatting and linting
poetry run black src tests
poetry run flake8 src tests

# Add additional dependencies
poetry add <dependency-name>
poetry add --dev <dev-dependency-name>
```

## Further Readings

1. [Proper Python Project Structure 2024](https://matt.sh/python-project-structure-2024)
2. [The Hitchhiker's Guide to Python - Structuring Your Project](https://docs.python-guide.org/writing/structure/)
3. [Real Python - Python Application Layouts: A Reference](https://realpython.com/python-application-layouts/)
4. [Ultimate Python Project Directory Structure Guide for Python Projects](https://www.codewithc.com/ultimate-python-project-directory-structure-guide-for-python-projects/)
