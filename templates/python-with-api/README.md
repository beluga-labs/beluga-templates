# beluga labs – Python with FastAPI Template

This project is a template for a modern FastAPI application built with Python. It includes the following features:

- **FastAPI** as the web framework.
- **Uvicorn** as the ASGI server.
- **SQLAlchemy 2** for database connectivity.
- **Alembic** for database migrations.
- **Pydantic** for data validation and schema management.
- Environment configuration managed via a `.env` file (using python-dotenv).
- Optional features such as token-based authentication, rate limiting, centralized logging, and more.

## Prerequisites

Make sure you have installed:

- **Python 3.9+** (preferably Python 3.10 or higher)
- **PostgreSQL** (or another supported database; adjust the configuration accordingly)
- Git and other necessary tools for cloning and managing the repository

## Package Management with PDM

This project uses [PDM](https://pdm.fming.dev/) (Python Development Master) as its package and environment manager.

PDM is a modern, lightweight alternative to `pip` + `venv` that supports PEP 582, lockfiles, and a declarative `pyproject.toml`.

> All dependencies and scripts are managed through PDM.

### 📥 Install PDM

#### macOS (Homebrew):

```bash
brew install pdm
```

#### macOS or Linux (via curl):

```bash
curl -sSL https://pdm-project.org/install-pdm.py | python3 -
```

#### Windows:

```bash
powershell -ExecutionPolicy ByPass -c "irm https://pdm-project.org/install-pdm.py | py -"
```

## Installation

1. **Set up the project environment using PDM:**

PDM handles virtual environments and dependency management automatically.
You do **not** need to manually create or activate a `venv`.

If needed, PDM will create and manage a virtual environment for you.

1. **Install required packages:**

    ```bash
    pdm install
    ```

## Configuration

1. **Set up the .env file:**

   In the project root, create a file named `.env` with the following content (adjust the values as needed):

   ```env
   DATABASE_URL="postgresql+psycopg2://username:password@localhost:5432/yourdatabase"
   ````

2. **Application settings:**

   Central settings are managed in `app/core/settings.py`. Verify that all necessary configurations are set.

## Database Migrations

1. **Create a new migration (if you modify your models):**

   ```bash
   alembic revision --autogenerate -m "Migration message describing the changes"
   ```

2. **Apply the migration:**

   ```bash
   alembic upgrade head
   ```

   Note: If working in a development environment and you need to rebuild your database, you might also use:

   ```bash
   alembic downgrade base
   alembic upgrade head
   ```

## Running the Application

1. **Start via run.py:**

   ```bash
   pdm run python run.py
   ```

2. **Direct start with Uvicorn:**

   ```bash
   pdm run uvicorn app.main:app --reload
   ```

## Running Tests

   ```bash
   pdm run pytest
   ```

## List current dev dependencies

   ```bash
   pdm list --group dev
   ```

## Code Formatting & Linting

This project uses the following tools to maintain clean, consistent, and correct code:

- 🦊 **[Ruff](https://docs.astral.sh/ruff/)** – for linting, import sorting (isort-style), and formatting
- 🧠 **[Mypy](http://mypy-lang.org/)** – for static type checking using Python's type hints

### Install development dependencies

```bash
pip install -r requirements-dev.txt
```

### Run Ruff (lint + fix imports + style)

```bash
# Check code quality
pdm run ruff check .

# Automatically fix linting issues
pdm run ruff check . --fix

# Format code (Ruff formatter)
pdm run ruff format .
```

### Run Mypy (type checking)

```bash
pdm run mypy .
```

## Reproducible Installs

PDM uses `pdm.lock` to lock dependency versions. To install exactly those versions:

```bash
pdm install
```

To refresh the lockfile (e.g. after adding or updating dependencies):

```bash
pdm lock
```

## Additional Notes

- **Logging:**
  Centralized logging is defined in `app/core/logger.py`. Adjust the log levels and formats as needed.

- **Authentication & Rate Limiting:**
  The project includes token-based authentication and rate limiting mechanisms. Review the files `app/core/security.py` and `app/core/limiter.py` to customize these features.

- **Extensibility:**
  The modular project structure allows for easy integration of additional modules, such as background tasks, new API routes, or middleware.
