from typing import Optional, List
from enum import Enum
from pydantic import BaseModel

class TaskBase(BaseModel):
    id: int
    gps_latitude: float
    gps_longitude: float
        
    class Config:
        orm_mode = True

class NewTaskFullReturn(BaseModel):
    code: Optional[int]
    msg: Optional[str]
    item_geojson_type: Optional[str]
    item_geojson_geometry_type: Optional[str]
    item_order_id: Optional[int]
    item_geojson_geometry_coordinates: Optional[List[float]]
    item_geojson_properties_name: Optional[str]
    total: Optional[int]
    input_battery: float
    input_distance: float
    input_weigth: float
    input_volume: float

# class TaskBase(BaseModel):
#     id: int
#     gps_latitude: float
#     gps_longitude: float
        
#     class Config:
#         orm_mode = True


# class GeoJSONGeometry(BaseModel):
#     geometry_type: str = "Point"
#     coordinates: List[float]

# # class GeoJSONProperties(BaseModel):
# #     name: str = "Moscow"

# class GeoJSON(BaseModel):
#     geojson_type: str = "Feature"
#     geometry: Optional[GeoJSONGeometry]
#     properties: dict = {"name": "Moscow"}

# class TaskGeoJSON(BaseModel):
#     id: int
#     geojson: Optional[GeoJSON]

# class DroneInput(BaseModel):
#     battery: int
#     distance = 200
#     weight = 800
#     volume = 20

# class NewTaskFullReturn(BaseModel):
#     code: int
#     msg: str
#     item: TaskGeoJSON
#     droneinput: Optional[DroneInput]

