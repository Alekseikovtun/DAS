#!/usr/bin/env python3
from typing import Optional
from dotenv import load_dotenv
import typer

load_dotenv(".env")

app = typer.Typer(add_completion=False)

@app.command(
    help="Run the latest migrations."
)
def migrate():
    typer.echo("Migrating")
    import alembic.config #вот тут я б разобрался
    alembicArgs = [
        '--raiseerr',
        'upgrade', 'head',
    ]
    alembic.config.main(argv=alembicArgs)


@app.command(
    help="Create new migrations"
)
def create_migrations(message: Optional[str] = typer.Argument("new migrations")):
    typer.echo(f"Creating migration '{message}'")
    import alembic.config
    alembicArgs = [
        '--raiseerr',
        'revision', '--autogenerate', "-m", message,
    ]
    alembic.config.main(argv=alembicArgs)

@app.command(
    help="DB values Initialization"
)
def init_values():
    from crud.crud_session import connection_string_direct
    import sqlalchemy as sa
    from sqlalchemy.sql import text
    engine = sa.create_engine(connection_string_direct)
    conn = engine.connect()
    # c = conn.cursor()
    fd = open('Init_values.sql', 'r')
    sqlFile = fd.read()
    fd.close()

    sqlCommands = sqlFile.split(';')

    for command in sqlCommands:
        try:
            conn.execute(command)
        except Exception as ex:
            print(f'Command skipped. {command=}, {str(ex)=}')


if __name__ == "__main__":
    # migrate()
    # create_migrations()
    app()