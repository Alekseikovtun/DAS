from typing import Any, Dict

import sqlalchemy as sa
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker

from config import db_config
from models.drone import DroneStatus
from models.station import Task
from schemas.drone_task_schema import TaskToDrone, TaskToAdmin

db = f"""postgresql://\
{db_config.POSTGRES_USER}:{db_config.POSTGRES_PASSWORD}\
@localhost:{db_config.POSTGRES_OUT_PORT}/{db_config.DB_NAME}"""
engine = sa.create_engine(db)
Session = sessionmaker(bind=engine)
connection = engine.connect()
session = Session()


def read_data_for_new_task(user) -> Dict[str, Any]:
    resp = session.query(func.min(Task.id)).filter(
        Task.task_status_id == 1
    ).scalar()
    next_task: Task = session.query(Task).filter(Task.id == resp).all()[0]
    if user == 'admin':
        result = TaskToAdmin.from_orm(next_task)
    if user == 'drone':
        result = TaskToDrone.from_orm(next_task)
    if user != 'admin' or 'drone':
        result = 'Not enough rights'
    return result


def add_task_to_db(user, add_latitude, add_longitude, add_priority):
    if user == 'user' or 'admin':
        last_coord_id = session.query(func.max(Task.id)).scalar()
        new_coord = Task(
            id=last_coord_id+1,
            latitude=add_latitude,
            longitude=add_longitude,
            task_status_id=1,
            priority=add_priority
        )
        session.add_all([new_coord])
        session.commit()
        result = (
            f'The data is entered.\n'
            f'Latitude is {add_latitude}\n'
            f'Longitude is {add_longitude}\n'
            f'Priority: {add_priority}\n'
        )
    else:
        result = 'Not enough rights'
    return result


def add_dron_status(user, drone_id, battery, departure_lat, departure_long):
    if user == 'DB' or 'admin':
        new_info = DroneStatus(
            id=drone_id,
            battery_charge_lvl=battery,
            departure_latitude=departure_lat,
            departure_longitude=departure_long
        )
        session.add_all([new_info])
        session.commit()
        result = 'Information about the drone has been received\n'
    else:
        result = 'The database updates the data automatically'
    return result


def update_task_info(departure_lat, departure_long):
    try:
        task_status_update = session.query(Task).filter(
            Task.latitude == departure_lat,
            Task.longitude == departure_long
        )
        record = task_status_update.one()
        record.task_status_id = 3
        session.commit()
        result = 'The task status has been updated\n'
    except Exception:
        result = 'Attention! A drone with an unknown task \n'
    return result
