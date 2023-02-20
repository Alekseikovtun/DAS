from datetime import datetime

from sqlalchemy import (
    func, Integer, String, TIMESTAMP, Column, Float, ForeignKey
    )
from config.base import Base
from models.drone import Drone, DroneType
from models.log import DroneLog
from sqlalchemy.orm import relationship
from enum import Enum

class TaskStatus(str, Enum):
    NEW = "NEW"
    IN_PROGRESS = "IN PROGRESS"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"

class Flight(Base):
    __tablename__ = "flight"

    id = Column(Integer, primary_key=True)
    started_at = Column(TIMESTAMP(timezone=True))
    finished_at = Column(TIMESTAMP(timezone=True))
    estimated_at = Column(TIMESTAMP(timezone=True))
    deviation = Column(Float)

    tasks = relationship('Task', backref='flight')
    cargos = relationship('Cargo', backref='flight')

class Cargo(Base):
    __tablename__ = "cargo"

    id = Column(Integer, primary_key=True)
    weight = Column(Float)
    volume = Column(Float)
    name = Column(String)

    tasks = relationship('Task', backref='cargo')
    id_drone_type = Column(Integer, ForeignKey(DroneType.id))
    id_flight = Column(Integer, ForeignKey(Flight))

class Task(Base):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True)
    created_at = Column(TIMESTAMP(timezone=True), default=func.now())
    updated_at: datetime = Column(
        TIMESTAMP(timezone=True),
        default=func.now(),
        onupdate=func.now()
    )
    gps_latitude = Column(Float)
    gps_longitude = Column(Float)
    priority = Column(String)
    task_status: TaskStatus = Column(String, nullable=False)
    completed_at = Column(TIMESTAMP(timezone=True))

    id_drone = Column(Integer, ForeignKey(Drone.id))
    id_cargo = Column(Integer, ForeignKey(Cargo.id))
    id_flight = Column(Integer, ForeignKey(Flight.id))

class Alert(Base):
    __tablename__ = "alert"

    name = Column(String, primary_key=True)
    solution = Column(String)
    
    log = Column(Integer, ForeignKey(DroneLog.id))