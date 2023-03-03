from fastapi import APIRouter, Depends
from service import station
from schemas.station_schema import TaskBase
from schemas.station_task_schema import Task
from models.station import Task as ModelTask
from sqlalchemy.ext.asyncio import AsyncSession
from crud import get_db

router = APIRouter()


@router.get('/new_task/', response_model=TaskBase)
async def read_data_for_new_task(
    db: AsyncSession = Depends(get_db)
) -> TaskBase:
    task: ModelTask = await station.read_data_for_new_task(db)
    result: TaskBase = TaskBase.from_orm(task)
    return result


@router.post('/add_coord', response_model=TaskBase)
async def add_task_to_db(
    task: Task,
    db: AsyncSession = Depends(get_db)
) -> TaskBase:
    new_task = await station.add_task_to_db(db, task.gps_latitude, task.gps_longitude, task.priority, task.task_status)
    result: TaskBase = TaskBase.from_orm(new_task)
    return result
