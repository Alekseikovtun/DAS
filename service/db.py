import sqlalchemy as sa
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker

from config import db_config
from models.station import Task

db = f'postgresql://{db_config.POSTGRES_USER}:{db_config.POSTGRES_PASSWORD}@localhost:{db_config.POSTGRES_OUT_PORT}/postgres'
engine = sa.create_engine(db)
Session = sessionmaker(bind=engine)
connection = engine.connect()
session = Session()


def read_data_for_new_task():
    pass


def add_coordinate_to_db(add_latitude, add_longitude):
    last_coord = session.query(Task, func.max(Task.id)).group_by(Task.id)
    last_id = last_coord.all()[0][1]
    new_coord = Task(id=last_id+1, latitude=add_latitude, longitude=add_longitude, task_status_id=1)
    session.add_all([new_coord])
    session.commit()


def add_dron_info():
    pass
