from invoke import task

@task
def install(c):
    """Install dependencies"""
    c.run("poetry install")

@task
def format(c):
    """Format code with black and isort"""
    c.run("poetry run black src tests")
    c.run("poetry run isort src tests")

@task
def lint(c):
    """Run linting"""
    c.run("poetry run flake8 src tests")
    c.run("poetry run mypy src")

@task
def test(c):
    """Run tests"""
    c.run("poetry run pytest")

@task
def clean(c):
    """Clean build artifacts"""
    c.run("rm -rf dist/ build/ *.egg-info/")
    c.run("find . -type d -name __pycache__ -delete")

@task
def build(c):
    """Build package"""
    c.run("poetry build")

@task(pre=[format, lint, test])
def check(c):
    """Run all checks"""
    print("All checks passed!")
