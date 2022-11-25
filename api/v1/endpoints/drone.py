from fastapi import APIRouter
from service import drone
from schemas.station_schema import TaskBase
from schemas.drone_schema import Drone

router = APIRouter()


@router.post('/add_drone_info', response_model=TaskBase)
async def add_drone_status(drone_model: Drone) -> TaskBase:
    await drone.add_drone_status(drone_model.drone_id, drone_model.battery, drone_model.d_latitude, drone_model.d_longitude)