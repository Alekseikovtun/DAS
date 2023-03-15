from pydantic import BaseModel

class Cargo(BaseModel):
    weight: float
    volume: float
    name: str

    class Config:
        orm_mode = True

class Task(BaseModel):
    gps_latitude: float
    gps_longitude: float
    priority: str
    task_status: str

    class Config:
        orm_mode = True
