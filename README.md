# Python Project

A production-ready Python project using Poetry for dependency management.

## Setup

Run the setup script to initialize the project:

```bash
./setup.sh
```

## Development

### Install dependencies
```bash
poetry install
```

### Activate virtual environment
```bash
poetry shell
```

### Available commands
```bash
poetry run invoke install  # Install dependencies
poetry run invoke format   # Format code with black and isort
poetry run invoke lint     # Run linting with flake8 and mypy
poetry run invoke test     # Run tests with pytest
poetry run invoke check    # Run all checks (format, lint, test)
poetry run invoke build    # Build package
```

### Run the application

**Option 1: Use the Poetry script (recommended)**
```bash
poetry run ram-ai-python
```

**Option 2: Run the main module directly**
```bash
poetry run python src/ram_ai_python/main.py
```

**Option 3: Use Python module syntax**
```bash
poetry run python -m ram_ai_python.main
```

## Requirements

- Python 3.8+
- Poetry
