from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

import os
from dotenv import load
from alembic import context

load()
# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

section=config.config_ini_section
DRIVER=os.getenv("DB_DRIVER")
DB_DRIVER=os.getenv("DB_DRIVER")
DB_username=os.getenv("DB_username")
DB_password=os.getenv("DB_password")
DB_HOST=os.getenv("DB_HOST")
DB_name=os.getenv("DB_name")
DB_port=os.getenv("DB_port")
SQLALCHEMY_URL=f'{DRIVER}://{DB_username}:{DB_password}@{DB_HOST}:{DB_port}/{DB_username}'
config.set_section_option(section, "sqlalchemy.url", SQLALCHEMY_URL)
# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
from users.models_users import User
from entry.models_entry import Entry
from competitions.models_comp import Competition
from database import Base
target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
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
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
