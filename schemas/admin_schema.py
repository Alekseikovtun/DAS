from pydantic import BaseModel
from typing import Optional


class TaskStatus(BaseModel):
    task_status: str


class MainTaskInfo(TaskStatus):
    id: int
    gps_latitude: float
    gps_longitude: float
    priority: str
    code: Optional[int]
    msg: Optional[str]

    class Config:
        orm_mode = True


class UnrealStatus(BaseModel):
    task_id: int
    msg: str
    code: Optional[int]


class SetUnrealStatus(TaskStatus):
    task_id: int
