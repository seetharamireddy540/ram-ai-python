#!/bin/bash
set -e

echo "Setting up Python project..."

# Check if Poetry is installed
if ! command -v poetry &> /dev/null; then
    echo "Poetry not found. Installing Poetry..."
    curl -sSL https://install.python-poetry.org | python3 -
    export PATH="$HOME/.local/bin:$PATH"
fi

# Create virtual environment and install dependencies
echo "Creating virtual environment and installing dependencies..."
poetry install

# Create src directory structure
mkdir -p src tests

echo "Setup complete!"
echo ""
echo "Available commands:"
echo "  poetry run invoke install  - Install dependencies"
echo "  poetry run invoke format   - Format code"
echo "  poetry run invoke lint     - Run linting"
echo "  poetry run invoke test     - Run tests"
echo "  poetry run invoke check    - Run all checks"
echo "  poetry run invoke build    - Build package"
echo ""
echo "To activate the virtual environment:"
echo "  poetry shell"
