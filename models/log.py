from sqlalchemy import (
    Column, Integer, TIMESTAMP, func, ForeignKey, VARCHAR, TEXT)
from models.base import Base
from sqlalchemy.orm import relationship


class Log(Base):
    __tablename__ = "log"

    id = Column(Integer, primary_key=True)
    created_at = Column(TIMESTAMP(timezone=True), default=func.now())
    log_content = Column(TEXT)  


class DroneLog(Base):
    __tablename__ = "drone_log"

    id = Column(Integer, primary_key=True)
    log_content = Column(TEXT)

    alerts = relationship('Alert', uselist=False)
    id_task = Column(Integer, ForeignKey('task.id'))


class Alert(Base):
    __tablename__ = "alert"

    name = Column(VARCHAR(255), primary_key=True)
    solution = Column(TEXT)

    log = Column(Integer, ForeignKey(DroneLog.id))


class AllLogs(Base):
    __tablename__ = "all_logs"

    id = Column(Integer, primary_key=True)
    created_at = Column(TIMESTAMP(timezone=True), default=func.now())
    log_type = Column(VARCHAR(255))
    context = Column(TEXT)
