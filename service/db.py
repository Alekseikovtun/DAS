import sqlalchemy as sa
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker

from config import db_config
from models.drone import DroneStatus
from models.station import Task

db = f'postgresql://{db_config.POSTGRES_USER}:{db_config.POSTGRES_PASSWORD}@localhost:{db_config.POSTGRES_OUT_PORT}/postgres'
engine = sa.create_engine(db)
Session = sessionmaker(bind=engine)
connection = engine.connect()
session = Session()


def read_data_for_new_task():
    next_task = session.query(Task, func.min(Task.id)).filter(Task.task_status_id==1).group_by(Task.id)
    next = next_task.all()[-1][1]
    print(f'The next task has ID: {next}')


def add_coordinate_to_db(add_latitude, add_longitude):
    last_coord = session.query(func.max(Task.id)).scalar()
    new_coord = Task(id=last_coord+1, latitude=add_latitude, longitude=add_longitude, task_status_id=1)
    session.add_all([new_coord])
    session.commit()
    print('\n Data entered \n')


def add_dron_status(drone_id, battery, departure_lat, departure_long):
    try:
        new_info = DroneStatus(id=drone_id, battery_charge_lvl=battery, departure_latitude=departure_lat, departure_longitude=departure_long)
        session.add_all([new_info])
        session.commit()
        print('\n Information about the drone has been received \n')
        task_status_update = session.query(Task).filter(Task.latitude == departure_lat, Task.longitude == departure_long)
        record = task_status_update.one()
        record.task_status_id = 3
        session.commit()
        print('\n The task status has been updated \n')
    except:
        print('\n  Attention! A drone with an unknown task \n')
