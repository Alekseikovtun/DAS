from sqlalchemy import Column, Integer, String, TIMESTAMP, func, ForeignKey
from models.base import Base
# from models.station import Alert, Task
from sqlalchemy.orm import relationship


class Log(Base):
    __tablename__ = "log"

    id = Column(Integer, primary_key=True)
    created_at = Column(TIMESTAMP(timezone=True), default=func.now())
    log_content = Column(String)


class DroneLog(Base):
    __tablename__ = "drone_log"

    id = Column(Integer, primary_key=True)
    log_content = Column(String)

    # alerts = relationship(Alert, uselist=False)
    # id_task = Column(Integer, ForeignKey(Task.id))


class Alert(Base):
    __tablename__ = "alert"

    name = Column(String, primary_key=True)
    solution = Column(String)
    
    log = Column(Integer, ForeignKey(DroneLog.id))
