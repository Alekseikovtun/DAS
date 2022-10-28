from datetime import datetime

import sqlalchemy as sa
from sqlalchemy import func
from models.base import Base
from sqlalchemy.orm import relationship


class TaskStatus(Base):
    __tablename__ = 'task_status'
    id = sa.Column(sa.Integer, primary_key=True)
    status = sa.Column(sa.String(20))

    tasks = relationship('Task', backref='task_status')


class Task(Base):
    __tablename__ = 'task'
    created_at = sa.Column(sa.TIMESTAMP(timezone=True), default=func.now())
    updated_at: datetime = sa.Column(
        sa.TIMESTAMP(timezone=True),
        default=func.now(),
        onupdate=func.now()
    )
    id = sa.Column(sa.Integer, primary_key=True)
    latitude = sa.Column(sa.Float)
    longitude = sa.Column(sa.Float)

    task_status_id = sa.Column(sa.Integer, sa.ForeignKey('task_status.id'))
