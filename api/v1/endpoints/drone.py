from fastapi import APIRouter
from service import drone as d, station
from schemas.station_schema import TaskBase
from models.station import Task
from schemas.drone_schema import Drone

router = APIRouter()


@router.post('/add_drone_info', response_model=TaskBase)
async def add_drone_status(drone: Drone) -> TaskBase:
    await d.add_drone_status(drone.drone_id, drone.battery, drone.d_latitude, drone.d_longitude)
    ut_result: Task = await station.update_task_info(drone.d_latitude, drone.d_longitude)
    result: TaskBase = TaskBase.from_orm(ut_result)
    return result
