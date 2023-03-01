from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context
from config.pydantic_config import settings
from models import Base

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config1 = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config1.config_file_name is not None:
    fileConfig(config1.config_file_name)

conn_url = f"mysql://{settings.MYSQL_USER}:{settings.MYSQL_PASSWORD}@{settings.MYSQL_HOST}:{settings.MYSQL_OUT_PORT}/{settings.MYSQL_DATABASE}"
config1.set_main_option("sqlalchemy.url", conn_url)
# print("\n\n", f"{conn_url=}", "\n")

# add your model's MetaData object here
# for 'autogenerate' support
#from models.base import Base
target_metadata = (Base.metadata)
# target_metadata = Base.metadata
# target_metadata = None

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
    url = config1.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    # print("/n/n/n/n", f"{config1.get_section(config1.config_ini_section)=}", "/n/n/n")

    connectable = engine_from_config(
        config1.get_section(config1.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata, compare_type=True
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
