from sqlalchemy import Column, Integer, Float, String, ForeignKey
from models.base import Base
from models.station import Task, Cargo
from models.log import DroneLog
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
    cargos = relationship(Cargo, backref='drone_type')

class DroneStatus(str, Enum):
    FREE = "FREE"
    CHARGING = "CHARGING"
    FLYING = "FLYING"

class Drone(Base):
    __tablename__ = "drone"

    id = Column(Integer, primary_key=True)
    access_key = Column(String)
    drone_status: DroneStatus = Column(String, nullable=False) 
    place_number = Column(Integer)

    id_drone_type = Column(Integer, ForeignKey(DroneType.id))
    tasks = relationship(Task, backref='drone')
    logs = relationship(DroneLog, backref='drone')