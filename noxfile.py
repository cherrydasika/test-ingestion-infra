import nox

# Reuse the same Python version as your Poetry project
PYTHON_VERSION = "3.9"

# Dev tools
DEV_DEPENDENCIES = [
    "black",
    "isort",
    "flake8",
    "mypy",
    "pytest",
    "poetry",
]


@nox.session
def format(session):
    """Format code with black and isort."""
    session.install(*DEV_DEPENDENCIES)  # Install into Nox's virtualenv
    session.run("poetry", "run", "black", ".", external=True)  # Use Poetry's black
    session.run("poetry", "run", "isort", ".", external=True)  # Use Poetry's isort


@nox.session
def lint(session):
    """Lint with flake8."""
    session.install(*DEV_DEPENDENCIES)
    session.run("flake8", "src", "tests")


@nox.session
def typecheck(session):
    """Run mypy for type checking."""
    session.install(*DEV_DEPENDENCIES)
    session.run("mypy", "src")


@nox.session
def tests(session):
    """Run tests with pytest."""
    session.install("poetry")
    session.run("poetry", "install", "--with", "dev")
    session.run("pytest")


@nox.session
def all(session):
    """Run all checks."""
    session.notify("format")
    session.notify("lint")
    session.notify("typecheck")
    session.notify("tests")
