from pydantic import BaseModel


class Drone(BaseModel):
    drone_id: int
    battery: int
    d_latitude: float
    d_longitude: float