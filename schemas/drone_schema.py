from pydantic import BaseModel
from typing import Optional


class Drone(BaseModel):
    access_key: Optional[str]
    drone_status: Optional[str]
    place_number: Optional[int]
    id_drone_type: Optional[int]

    class Config:
        orm_mode = True

class DroneType(BaseModel):
    engine_power: float
    flight_range: float
    load_capacity: float
    cargo_volume: float
    battery_capacity: float