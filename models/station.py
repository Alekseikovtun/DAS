import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

import config.db_config as db_config

Base = declarative_base()

db = f'postgresql://{db_config.POSTGRES_USER}:{db_config.POSTGRES_PASSWORD}@localhost:{db_config.POSTGRES_OUT_PORT}/postgres'
engine = sa.create_engine(db)
Session = sessionmaker(bind=engine)
connection = engine.connect()


class DronStatus(Base):
    __tablename__ = 'dron_status'
    # created_at = sa.Column()
    # updated_at = sa.Column()
    id = sa.Column(sa.Integer, primary_key=True)
    battery_charge_lvl = sa.Column(sa.Integer)
    departure_latitude = sa.Column(sa.Integer)
    departure_longitude = sa.Column(sa.Integer)


class Task(Base):
    __tablename__ = 'task'
    # created_at = sa.Column()
    # updated_at = sa.Column()
    id = sa.Column(sa.Integer, primary_key=True)
    latitude = sa.Column(sa.Integer)
    longtitude = sa.Column(sa.Integer)

    task_statuses = relationship('TaskStatus', backref='task')


class TaskStatus(Base):
    __tablename__ = 'task_status'
    # created_at = sa.Column()
    # updated_at = sa.Column()
    id = sa.Column(sa.Integer, primary_key=True)
    status = sa.Column(sa.String(20))

    task_id = sa.Column(sa.Integer, sa.ForeignKey('task.id'))
