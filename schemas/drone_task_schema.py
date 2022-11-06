from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class DroneTaskBase(BaseModel):
    latitude: float
    longitude: float

    class Config:
        orm_mode = True


class TaskToDrone(DroneTaskBase):
    id: int


class TaskToAdmin(TaskToDrone):
    priority: Optional[str]
    task_status_id: int
    created_at: datetime
    updated_at: datetime
