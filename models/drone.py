import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class DroneStatus(Base):
    __tablename__ = 'drone_status'
    # created_at = sa.Column()
    # updated_at = sa.Column()
    id = sa.Column(sa.Integer, primary_key=True)
    battery_charge_lvl = sa.Column(sa.Integer)
    departure_latitude = sa.Column(sa.Integer)
    departure_longitude = sa.Column(sa.Integer)
