from pydantic import BaseModel
from typing import Optional


class Drone(BaseModel):
    access_key: str
    drone_status: str
    place_number: int
    id_drone_type: int

    class Config:
        orm_mode = True

class DroneType(BaseModel):
    engine_power: float
    flight_range: float
    load_capacity: float
    cargo_volume: float
    battery_capacity: float

class DroneAndTypeFull(BaseModel):
    drone_info: Optional[Drone]
    drone_type: Optional[DroneType]