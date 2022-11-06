from pydantic import BaseModel
from typing import Optional


class BaseSchema(BaseModel):
    latitude: float
    longitude: float
    priority: Optional[str]

    class Config:
        orm_mode = True
