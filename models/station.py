from datetime import datetime

from sqlalchemy import (
    func, Integer, String, TIMESTAMP, Column, Float, ForeignKey
    )
from models.base import Base
from sqlalchemy.orm import relationship


class TaskStatus(Base):
    __tablename__ = 'task_status'
    id = Column(Integer, primary_key=True)
    status = Column(String(20))

    tasks = relationship('Task', backref='task_status')


class Task(Base):
    __tablename__ = 'task'
    created_at = Column(TIMESTAMP(timezone=True), default=func.now())
    updated_at: datetime = Column(
        TIMESTAMP(timezone=True),
        default=func.now(),
        onupdate=func.now()
    )
    id = Column(Integer, primary_key=True)
    latitude = Column(Float)
    longitude = Column(Float)
    priority = Column(String(20))

    task_status_id = Column(Integer, ForeignKey('task_status.id'))
