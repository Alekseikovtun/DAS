from pydantic import BaseModel


class TaskBase(BaseModel):
    id: int
    gps_latitude: float
    gps_longitude: float

    class Config:
        orm_mode = True
