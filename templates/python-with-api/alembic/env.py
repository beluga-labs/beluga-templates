from logging.config import fileConfig
import os
from dotenv import load_dotenv

load_dotenv()

db_url = os.getenv("DATABASE_URL")
if not db_url:
    raise Exception("DATABASE_URL wurde in der .env Datei nicht gefunden!")

from sqlalchemy import engine_from_config, pool
from alembic import context

config = context.config

config.set_main_option("sqlalchemy.url", db_url)

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

from app.db.database import Base

# Import your models here to ensure they are registered with SQLAlchemy
from app.models.user import User
from app.models.token import Token

target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Executes migrations in 'offline' mode, i.e. without creating an engine."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Executes migrations in 'online' mode, i.e. with a generated engine."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
