from typing import Optional, List
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
