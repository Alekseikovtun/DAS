import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class TaskStatus(Base):
    __tablename__ = 'task_status'
    # created_at = sa.Column()
    # updated_at = sa.Column()
    id = sa.Column(sa.Integer, primary_key=True)
    status = sa.Column(sa.String(20))

    tasks = relationship('Task', backref='task_status')


class Task(Base):
    __tablename__ = 'task'
    # created_at = sa.Column()
    # updated_at = sa.Column()
    id = sa.Column(sa.Integer, primary_key=True)
    latitude = sa.Column(sa.Float)
    longitude = sa.Column(sa.Float)

    task_status_id = sa.Column(sa.Integer, sa.ForeignKey('task_status.id'))
