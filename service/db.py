import sqlalchemy as sa
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker

from models import station
from models.station import Task

engine = sa.create_engine(station.db)
Session = sessionmaker(bind=engine)
session = Session()


def read_data_for_new_task():
    pass


def add_coordinate_to_db():
    last_coord = session.query(Task, func.max(Task.id)).group_by(Task.id)
    last_id = last_coord.all()[0][1]
    add_latitude = input('Enter the latitude coordinates: ')
    add_longitude = input('Enter the longitude coordinates: ')
    new_coord = Task(id=last_id+1, latitude=add_latitude, longtitude=add_longitude)
    session.add_all([new_coord])
    session.commit()


def add_dron_info():
    pass
