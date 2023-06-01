from datetime import datetime
import sqlalchemy as sa
from sqlalchemy import (
    func, Integer, TIMESTAMP, Column, Float, ForeignKey, VARCHAR, TEXT,)
from models.base import Base
from models.drone import Drone
from sqlalchemy.orm import relationship
from enum import Enum


class TaskStatus(str, Enum):
    NEW = "NEW"
    IN_PROGRESS = "IN PROGRESS"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    OFFERING = "OFFERING"
    UNREAL = "UNREAL"


class Flight(Base):
    __tablename__ = "flight"

    id = Column(Integer, primary_key=True)
    started_at = Column(TIMESTAMP(timezone=True), default=func.now())
    finished_at: datetime = Column(TIMESTAMP(timezone=True))

    id_task = Column(Integer, ForeignKey('task.id'))


class Cargo(Base):
    __tablename__ = "cargo"

    id = Column(Integer, primary_key=True, autoincrement=True)
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
    task_status: TaskStatus = Column(VARCHAR(64), nullable=False)
    completed_at = Column(TIMESTAMP(timezone=True))

    id_drone = Column(Integer, ForeignKey(Drone.id))
    id_cargo = Column(Integer, ForeignKey(Cargo.id))
    flights = relationship('Flight', backref='task')
    logs = relationship('DroneLog', backref='task')


class ChargingPoint(Base):
    __tablename__ = "charging_point"

    id = Column(Integer, primary_key=True)
    power = Column(Float)

    drones = relationship('Drone', secondary='charging_point_to_drone')


ChargingPoint_to_Drone = sa.Table(
    'charging_point_to_drone', Base.metadata,
    sa.Column(
        'charging_point_id', sa.Integer, sa.ForeignKey('charging_point.id')),
    sa.Column('drone_id', sa.Integer, sa.ForeignKey('drone.id')),
    sa.Column('id', sa.Integer, primary_key=True),
)
