from typing import Optional, List
from enum import Enum
from pydantic import BaseModel


class TaskBase(BaseModel):
    id: int
    gps_latitude: float
    gps_longitude: float
        
    class Config:
        orm_mode = True


class GeoJSONGeometry(BaseModel):
    geometry_type: str = "Point"
    coordinates: List[float]

# class GeoJSONProperties(BaseModel):
#     name: str = "Moscow"

class GeoJSON(BaseModel):
    geojson_type: str = "Feature"
    geometry: Optional[GeoJSONGeometry]
    properties: dict = {"name": "Moscow"}

class TaskGeoJSON(BaseModel):
    id: int
    geojson: Optional[GeoJSON]

class DroneInput(BaseModel):
    battery: int
    distance = 200
    weight = 800
    volume = 20

class NewTaskFullReturn(BaseModel):
    code: int
    msg: str
    item: TaskGeoJSON
    droneinput: Optional[DroneInput]

