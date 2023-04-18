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
    code: Optional[int]
    msg: Optional[str]


class DroneSolution(BaseModel):
    drone_id: int
    task_id: int
    status_code: bool


class DroneTaskCompleted(BaseModel):
    drone_id: int
    task_id: int
    task_status: str
    drone_log: str


class DroneTaskCompletedAnswer(BaseModel):
    code: int
    msg: str
