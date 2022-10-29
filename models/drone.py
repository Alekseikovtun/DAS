from datetime import datetime

from sqlalchemy import func, Column, TIMESTAMP, Integer
from models.base import Base


class DroneStatus(Base):
    __tablename__ = 'drone_status'
    created_at = Column(TIMESTAMP(timezone=True), default=func.now())
    updated_at: datetime = Column(
        TIMESTAMP(timezone=True),
        default=func.now(),
        onupdate=func.now()
    )
    id = Column(Integer, primary_key=True)
    battery_charge_lvl = Column(Integer)
    departure_latitude = Column(Integer)
    departure_longitude = Column(Integer)
