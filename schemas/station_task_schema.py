from pydantic import BaseModel


class Task(BaseModel):
    latitude: float
    longitude: float
    priority: str