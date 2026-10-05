from alembic import context
from sqlalchemy import Engine, engine_from_config
from sqlalchemy.pool import NullPool


def run_migrations_offline() -> None:
    context.configure(
        url='',
        target_metadata=None,
        sqlalchemy_module_prefix='',
        literal_binds=True,
        dialect_opts={'paramstyle': 'named'},
        compare_type=True,
        compare_server_default=True,
        include_schemas=True,
    )
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    engine: Engine = engine_from_config(
        configuration={'sqlalchemy.url': ''},
        prefix='sqlalchemy.',
        poolclass=NullPool,
    )
    with engine.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=None,
            sqlalchemy_module_prefix='',
            compare_type=True,
            compare_server_default=True,
            include_schemas=True,
        )
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
