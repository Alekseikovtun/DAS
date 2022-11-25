from service.db import create_drone_status
from schemas.station_schema import TaskBase
from models.station import Task
from service.station import update_task_info


async def add_drone_status(drone_id, battery, departure_lat, departure_long):
    await create_drone_status(drone_id, battery, departure_lat, departure_long)
    ut_result: Task = await update_task_info(departure_lat, departure_long)
    result: TaskBase = TaskBase.from_orm(ut_result)
    return result
