from datetime import datetime

from sqlalchemy import (
    func, Integer, TIMESTAMP, Column, Float, ForeignKey, VARCHAR
    )
from models.base import Base
from models.drone import Drone
# from models.log import DroneLog
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
    id_task = Column(Integer, ForeignKey('task.id'))

class Cargo(Base):
    __tablename__ = "cargo"

    id = Column(Integer, primary_key=True)
    weight = Column(Float)
    volume = Column(Float)
    name = Column(VARCHAR(64))

    tasks = relationship('Task', backref='cargo')

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
    priority = Column(VARCHAR(64))
    task_status: TaskStatus = Column(VARCHAR(64), nullable=False)
    completed_at = Column(TIMESTAMP(timezone=True))

    id_drone = Column(Integer, ForeignKey(Drone.id))
    id_cargo = Column(Integer, ForeignKey(Cargo.id))
    flights = relationship('Flight', backref='task')
    logs = relationship('DroneLog', backref='task')

