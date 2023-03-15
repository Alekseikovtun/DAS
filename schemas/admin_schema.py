from pydantic import BaseModel
from typing import Optional

class TaskStatus(BaseModel):
    task_status: str

class MainTaskInfo(TaskStatus):
    id: int
    gps_latitude: float
    gps_longitude: float
    priority: str

    class Config:
        orm_mode = True
