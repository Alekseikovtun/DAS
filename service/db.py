import sqlalchemy as sa
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker

from config import db_config
from models.drone import DroneStatus
from models.station import Task


db = f"""postgresql://\
{db_config.POSTGRES_USER}:{db_config.POSTGRES_PASSWORD}\
@{db_config.DB_HOST}:{db_config.POSTGRES_OUT_PORT}/{db_config.DB_NAME}"""
engine = sa.create_engine(db)
Session = sessionmaker(bind=engine)
connection = engine.connect()
session = Session()


def read_data_for_new_task() -> Task:
    resp = session.query(func.min(Task.id)).filter(
        Task.task_status_id == 1
    ).scalar()
    next_task: Task = session.query(Task).filter(Task.id == resp).all()[0]
    return next_task


def add_task_to_db(add_latitude, add_longitude, add_priority) -> Task:
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
    return new_coord


def add_dron_status(drone_id, battery, departure_lat, departure_long):
    new_info = DroneStatus(
        id=drone_id,
        battery_charge_lvl=battery,
        departure_latitude=departure_lat,
        departure_longitude=departure_long
    )
    session.add_all([new_info])
    session.commit()


def update_task_info(departure_lat, departure_long) -> Task:
    task_status_update = session.query(Task).filter(
        Task.latitude == departure_lat,
        Task.longitude == departure_long
    )
    record: Task = task_status_update.one()
    record.task_status_id = 3
    session.commit()
    return record
