import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker

from config import db_config
from models.drone import DroneStatus


db = f"""postgresql://\
{db_config.POSTGRES_USER}:{db_config.POSTGRES_PASSWORD}\
@{db_config.POSTGRES_HOST}:{db_config.POSTGRES_OUT_PORT}/{db_config.POSTGRES_DB}"""
engine = sa.create_engine(db)
Session = sessionmaker(bind=engine)
connection = engine.connect()
session = Session()


async def create_drone_status(drone_id, battery, departure_lat, departure_long):
    new_info = DroneStatus(
        id=drone_id,
        battery_charge_lvl=battery,
        departure_latitude=departure_lat,
        departure_longitude=departure_long
    )
    session.add_all([new_info])
    session.commit()