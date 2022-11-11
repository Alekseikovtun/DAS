from pydantic import BaseModel


class TaskBase(BaseModel):
    id: int
    latitude: float
    longitude: float

    class Config:
        orm_mode = True
