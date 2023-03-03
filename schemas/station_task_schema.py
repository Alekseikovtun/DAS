from pydantic import BaseModel


class Task(BaseModel):
    id: int
    gps_latitude: float
    gps_longitude: float
    priority: str
    task_status: str