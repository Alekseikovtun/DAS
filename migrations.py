#!/usr/bin/env python3
from typing import Optional
# import typer

# app = typer.Typer(add_completion=False)

# @app.command(
#     help="Run the latest migrations."
# )
def migrate():
    #typer.echo("Migrating")
    import alembic.config #вот тут я б разобрался
    alembicArgs = [
        '--raiseerr',
        'upgrade', 'head',
    ]
    alembic.config.main(argv=alembicArgs)


# @app.command(
#     help="Create new migrations"
# )
#message: Optional[str] = typer.Argument("new migrations")
def create_migrations():
    #typer.echo(f"Creating migration '{message}'")
    import alembic.config
    alembicArgs = [
        '--raiseerr',
        'revision', '--autogenerate', "-m",
    ]
    alembic.config.main(argv=alembicArgs)


if __name__ == "__main__":
    migrate()
    create_migrations()
    # app()