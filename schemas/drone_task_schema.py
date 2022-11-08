from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class DroneTaskBase(BaseModel):
    latitude: float
    longitude: float

    class Config:
        orm_mode = True


class DroneTaskToDrone(DroneTaskBase):
    id: int


class DroneTaskToAdmin(DroneTaskToDrone):
    priority: Optional[str]
    task_status_id: int
    created_at: datetime
    updated_at: datetime
