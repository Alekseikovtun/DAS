from sqlalchemy import Column, Integer, TIMESTAMP, func, ForeignKey, VARCHAR
from models.base import Base
# from models.station import Alert, Task
from sqlalchemy.orm import relationship


class Log(Base):
    __tablename__ = "log"

    id = Column(Integer, primary_key=True)
    created_at = Column(TIMESTAMP(timezone=True), default=func.now())
    log_content = Column(VARCHAR(1024))


class DroneLog(Base):
    __tablename__ = "drone_log"

    id = Column(Integer, primary_key=True)
    log_content = Column(VARCHAR(64))

    alerts = relationship('Alert', uselist=False)
    id_task = Column(Integer, ForeignKey('task.id'))


class Alert(Base):
    __tablename__ = "alert"

    name = Column(VARCHAR(64), primary_key=True)
    solution = Column(VARCHAR(64))
    
    log = Column(Integer, ForeignKey(DroneLog.id))
