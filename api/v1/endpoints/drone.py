from fastapi import APIRouter
from service import db
from schemas.station_schema import TaskBase
from models.station import Task
from schemas.drone_schema import Drone

router = APIRouter()


@router.post('/add_drone_info', response_model=TaskBase)
async def add_dron_status(drone: Drone) -> TaskBase:
    await db.add_dron_status(drone.drone_id, drone.battery, drone.d_latitude, drone.d_longitude)
    ut_result: Task = await db.update_task_info(drone.d_latitude, drone.d_longitude)
    result: TaskBase = TaskBase.from_orm(ut_result)
    return result
