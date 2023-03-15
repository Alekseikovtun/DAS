from sqlalchemy import Column, Integer, Float, ForeignKey, VARCHAR
from models.base import Base
# from models.station import Task
from sqlalchemy.orm import relationship
from enum import Enum


class DroneType(Base):
    __tablename__ = "drone_type"

    id = Column(Integer, primary_key=True)
    engine_power = Column(Float)
    flight_range = Column(Float)
    load_capacity = Column(Float) 
    cargo_volume = Column(Float)
    battery_capacity = Column(Float)

    drones = relationship('Drone', backref='drone_type')

class DroneStatus(str, Enum):
    FREE = "FREE"
    CHARGING = "CHARGING"
    FLYING = "FLYING"

class Drone(Base):
    __tablename__ = "drone"

    id = Column(Integer, primary_key=True)
    access_key = Column(VARCHAR(64))
    drone_status: DroneStatus = Column(VARCHAR(64), nullable=False) 
    place_number = Column(Integer)

    id_drone_type = Column(Integer, ForeignKey(DroneType.id))
    tasks = relationship('Task', backref='drone')
    charging_points = relationship('ChargingPoint', secondary='charging_point_to_drone')