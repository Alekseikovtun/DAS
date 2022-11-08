from fastapi import APIRouter
from service import db
from schemas.station_schema import TaskBase
from models.station import Task

router = APIRouter()


@router.post('/add_drone_info', response_model=TaskBase)
def add_dron_status(
    drone_id: int,
    battery: int,
    d_latitude: float,
    d_longitude: float
) -> TaskBase:
    db.add_dron_status(drone_id, battery, d_latitude, d_longitude)
    ut_result: Task = db.update_task_info(d_latitude, d_longitude)
    result: TaskBase = TaskBase.from_orm(ut_result)
    return result
