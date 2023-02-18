from sqlalchemy import Column, Integer, Float, String
from models.base import Base


class Drone(Base):
    __tablename__ = "drone"

    id = Column(Integer, primary_key=True)
    access_key = Column(String)
    status = Column(String)    
    place_number = Column(Integer)

class DroneType(Base):
    __tablename__ = "drone_type"

    id = Column(Integer, primary_key=True)
    engine_power = Column(Float)
    flight_range = Column(Float)
    load_capacity = Column(Float) 
    cargo_volume = Column(Float)
    battery_capacity = Column(Float)

class Logs(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True)
    log_content = Column(String)

class Reason(Base):
    __tablename__ = "reason"

    name = Column(String, primary_key=True)
    solution = Column(String)