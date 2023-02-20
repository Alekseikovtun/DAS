from sqlalchemy import Column, Integer, String, TIMESTAMP, func, ForeignKey
from models.base import Base
from models.drone import Drone
from models.station import Alert
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

    id_drone = Column(Integer, ForeignKey(Drone.id))
    alerts = relationship(Alert, uselist=False)

