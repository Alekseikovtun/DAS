from datetime import datetime

from sqlalchemy import (
    func, Integer, String, TIMESTAMP, Column, Float, ForeignKey
    )
from models.base import Base
from sqlalchemy.orm import relationship


class Task(Base):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True)
    created_at = Column(TIMESTAMP(timezone=True), default=func.now())
    updated_at: datetime = Column(
        TIMESTAMP(timezone=True),
        default=func.now(),
        onupdate=func.now()
    )
    delivery_latitude = Column(Float)
    delivery_longitude = Column(Float)
    priority = Column(String)
    status = Column(String)
    completed_at = Column(TIMESTAMP(timezone=True))

class Cargo(Base):
    __tablename__ = "cargo"

    id = Column(Integer, primary_key=True)
    weight = Column(Float)
    volume = Column(Float)
    name = Column(String)

class Delivery(Base):
    __tablename__ = "delivery"

    id = Column(Integer, primary_key=True)
    started_at = Column(TIMESTAMP(timezone=True))
    flight_time = Column(Integer) #???
    edt = Column(TIMESTAMP(timezone=True)) #estimated delivery time
    deviation = Column(Float)
